from db.stats_service import StatsService
from flask_restx import Resource, Namespace, reqparse
from zmb_labels import ZmbLabels

search_parser = reqparse.RequestParser()
for label in ZmbLabels.Article.Entity.all_labels_n_metainfo():
    search_parser.add_argument(label, type=str)

ns_desc = \
"""
This namespace is related to services that offers statistics about the entities
"""
stats = Namespace('Statistics', description=ns_desc)

@stats.route("/entities")
class StatsResource(Resource):
    """
    This class receives the HTTP requests and redirect them to the respective service
    """
    @stats.expect(search_parser)
    @stats.response(200, "Success")
    def get(self):
        """
        Counts the number of entities per entity type
        """
        criteria = search_parser.parse_args()
        with StatsService() as service:
            result_map = service.count_entities(criteria)
        return result_map

@stats.route("/summary")
class EntityFrequencyCounter(Resource):
    @stats.response(200, "Success")
    def get(self):
        """
        Counts the ocurrences of the most common entities
        """
        with StatsService() as service:
            result_map = service.count_ents_by_freq()
        return result_map
