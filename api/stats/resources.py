from db.stats_service import StatsService
from flask_restx import Resource, Namespace

ns_desc = \
"""
This namespace is related to services that offers statistics about the entities
"""

stats = Namespace('Statistics', description=ns_desc)

@stats.route("/count/entities")
class StatsResource(Resource):
    """
    This class receives the HTTP requests and redirect them to the respective service
    """

    @stats.response(200, "Success")
    def get(self):
        """
        Counts the number of entities per entity type
        """
        with StatsService() as service:
            result_map = service.count_entities()

        return result_map
