from sqlalchemy import Column, Integer, BigInteger, String, Date, Text
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from constants import API_KEY_SIZE
from labels import *
from .max_columns_sizes import *

Base = declarative_base()

class TableUsers(Base):
    __tablename__ = "tb_users"
    __table_args__ = (UniqueConstraint('code', name="codx_1"),)
    id = Column('id', Integer, primary_key=True)
    code = Column('code', String(12))
    name = Column('name', String(50), nullable=False)
    api_key = Column('api_key', String(API_KEY_SIZE), nullable=False)
    perm_level = Column('perm_level', Integer, nullable=False)

class TableArticles(Base):
    __tablename__ = "tb_articles"
    __table_args__ = (UniqueConstraint('hashed_url', name="urlx_1"),)
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, nullable=False)
    url = Column('url', Text(MAX_URL), nullable=False)
    content = Column('content', Text(MAX_CONTENT), nullable=False)
    published_time = Column('published_time', Date)
    title = Column('title', Text(MAX_CONTENT), nullable=False)
    keywords = Column('keywords', String(MAX_KEYWORDS))
    section = Column('section', String(MAX_SECTION))
    site_name = Column('site_name', String(MAX_SITE_NAME))
    source = Column('source', String(MAX_ENTITY_NAME_FIELD))
    authors = Column('authors', String(MAX_AUTHORS))
    added = Column('added', Date)
    last_modified = Column('last_modified', Date)
    miner = Column('miner', String(12))

class TableSources(Base):
    __tablename__ = "tb_sources"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)

class TableMedia(Base):
    __tablename__ = "tb_media"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableMovements(Base):
    __tablename__ = "tb_movements"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TablePeople(Base):
    __tablename__ = "tb_people"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableEducationalInstitutions(Base):
    __tablename__ = "tb_educ_inst"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('title', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TablePrivateInstitutions(Base):
    __tablename__ = "tb_private_inst"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('title', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TablePublicInstitutions(Base):
    __tablename__ = "tb_public_inst"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('title', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableRacistActions(Base):
    __tablename__ = "tb_racist_actions"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableWorks(Base):
    __tablename__ = "tb_works"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableCities(Base):
    __tablename__ = "tb_cities"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableStates(Base):
    __tablename__ = "tb_states"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableCountries(Base):
    __tablename__ = "tb_countries"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")

class TableLaws(Base):
    __tablename__ = "tb_laws"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    title = Column('title', String(MAX_ENTITY_NAME_FIELD))
    code = Column('code', String(MAX_ENTITY_NAME_FIELD))
    table_articles = relationship("TableArticles")

class TablePolices(Base):
    __tablename__ = "tb_polices"
    id = Column('id', Integer, primary_key=True)
    hashed_url = Column('hashed_url', BigInteger, ForeignKey('tb_articles.hashed_url'), nullable=False)
    name = Column('name', String(MAX_ENTITY_NAME_FIELD), nullable=False)
    table_articles = relationship("TableArticles")
