from sqlalchemy import (
    Column, Integer, BigInteger, String, Date, Text, Boolean
)
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from constants import API_KEY_SIZE
from .max_columns_sizes import *

Base = declarative_base()

class TableUsers(Base):
    __tablename__ = "tb_users"
    __table_args__ = (UniqueConstraint('code'),
                        {'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'})

    id = Column('id', Integer, primary_key=True)
    code = Column('code', String(12))
    name = Column('name', String(50), nullable=False)
    api_key = Column('api_key', String(API_KEY_SIZE), nullable=False)
    perm_level = Column('perm_level', Integer, nullable=False)

class TableArticles(Base):
    __tablename__ = "tb_articles"
    __table_args__ = (UniqueConstraint('hashed_url'),
                        {'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'})

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), nullable=False)
    url = Column('url', Text(MAX_URL), nullable=False)
    content = Column('content', Text(MAX_CONTENT), nullable=False)
    published_time = Column('published_time', Date)
    title = Column('title', Text(MAX_TITLE))
    keywords = Column('keywords', String(MAX_KEYWORDS))
    section = Column('section', String(MAX_SECTION))
    site_name = Column('site_name', String(MAX_SITE_NAME))
    authors = Column('authors', String(MAX_AUTHORS))
    html = Column('html', Text(MAX_HTML))
    meta_data = Column('meta_data', Text(MAX_METADATA))
    added = Column('added', Date)
    last_modified = Column('last_modified', Date)
    miner = Column('miner', String(12))

class TableSources(Base):
    __tablename__ = "tb_sources"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    #home_url = Column('home_url', String(MAX_URL))
    #enabled = Column('enabled', Boolean, nullable=False)
    table_articles = relationship("TableArticles")

class TableMedia(Base):
    __tablename__ = "tb_media"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableMovements(Base):
    __tablename__ = "tb_movements"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TablePeople(Base):
    __tablename__ = "tb_people"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableEducationals(Base):
    __tablename__ = "tb_educationals"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('title', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TablePrivates(Base):
    __tablename__ = "tb_privates"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('title', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TablePublics(Base):
    __tablename__ = "tb_publics"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('title', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableActions(Base):
    __tablename__ = "tb_actions"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableWorks(Base):
    __tablename__ = "tb_works"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableCities(Base):
    __tablename__ = "tb_cities"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableStates(Base):
    __tablename__ = "tb_states"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableCountries(Base):
    __tablename__ = "tb_countries"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableLaws(Base):
    __tablename__ = "tb_laws"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD))
    code = Column('code', String(MAX_ENTITY_NAME_FIELD))
    table_articles = relationship("TableArticles")

class TablePolices(Base):
    __tablename__ = "tb_polices"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TablePoliticals(Base):
    __tablename__ = "tb_parties"
    __table_args__ = ({'mysql_default_charset': 'utf8mb4',
                         'mysql_collate': 'utf8mb4_unicode_ci'},)

    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', String(HASH_SIZE), ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")
