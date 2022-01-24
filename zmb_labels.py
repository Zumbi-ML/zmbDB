# -*- coding: UTF-8 -*-

class ZmbLabels:

    class Article:

        class Source:
            def api():
                return "sources"

        class Title:
            def api():
                return "title"

        class Keyword:
            def api():
                return "keywords"

        class Section:
            def api():
                return "section"

        class Site:
            def api():
                return "site_name"

        class Author:
            def api():
                return "authors"

        class Entity:

            def api():
                return "entities"

            class City:
                def api():
                    return "cities"

            class Country:
                def api():
                    return "countries"

            class State:
                def api():
                    return "states"

            class Private:
                def api():
                    return "private"

            class Educational:
                def api():
                    return "educational"

            class Public:
                def api():
                    return "public"

            class Police:
                def api():
                    return "polices"

            class Law:
                def api():
                    return "laws"

            class People:
                def api():
                    return "people"

            class Movement:
                def api():
                    return "movements"

            class Political:
                def api():
                    return "political"

            class Media:
                def api():
                    return "media"

            class Work:
                def api():
                    return "works"

            def _all_classes():
                """
                Returns the classes of all the entities
                """
                return [ \
                    ZmbLabels.Article.Entity.City,
                    ZmbLabels.Article.Entity.Country,
                    ZmbLabels.Article.Entity.State,
                    ZmbLabels.Article.Entity.Private,
                    ZmbLabels.Article.Entity.Educational,
                    ZmbLabels.Article.Entity.Public,
                    ZmbLabels.Article.Entity.Police,
                    ZmbLabels.Article.Entity.Law,
                    ZmbLabels.Article.Entity.People,
                    ZmbLabels.Article.Entity.Movement,
                    ZmbLabels.Article.Entity.Political,
                    ZmbLabels.Article.Entity.Media,
                    ZmbLabels.Article.Entity.Work,
                ]

            def all_labels():
                """
                Returns the labels for all the entities:
                    E.g., ["cities", "states", "countries", ...]
                """
                return [class_.api() \
                        for class_ in ZmbLabels.Article.Entity._all_classes()]

            def all_labels_n_metainfo():
                """
                Returns the labels for all the entities PLUS relevant meta
                information about the article such as "sources"
                (which is not considered an entity per se)
                """
                return ZmbLabels.Article.Entity.all_labels() + \
                                                [ZmbLabels.Article.Source.api()]

        class Content:
            def api():
                return "content"

        class Miner:
            def api():
                return "miner"

        class PublishedTime:
            def api():
                return "published_time"

        class URL:
            def api():
                return "url"

        class HashedURL:
            def api():
                return "hashed_url"

        class HTML:
            def api():
                return "html"

        class Metadata:
            def api():
                return "meta_data"

        def all_labels():
            """
            Returns the API labels for the article's meta information
            """
            return [class_.api() \
                    for class_ in ZmbLabels.Article._all_classes()]

        def _all_classes():
            """
            Returns all the classes for the article's meta information
            """
            return [ \
                ZmbLabels.Article.Source,
                ZmbLabels.Article.Title,
                ZmbLabels.Article.Keyword,
                ZmbLabels.Article.Section,
                ZmbLabels.Article.Site,
                ZmbLabels.Article.Author,
                ZmbLabels.Article.Entity,
                ZmbLabels.Article.Content,
                ZmbLabels.Article.Miner,
                ZmbLabels.Article.PublishedTime,
                ZmbLabels.Article.URL,
                ZmbLabels.Article.HTML,
                ZmbLabels.Article.Metadata,
                ZmbLabels.Article.Miner,
            ]
