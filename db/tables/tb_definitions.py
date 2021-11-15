from sqlalchemy import Column, Integer, BigInteger, String, Date, Text
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from constants import API_KEY_SIZE

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
    __table_args__ = (UniqueConstraint('hashed_uri', name="urix_1"),)
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, nullable=False)
    uri = Column('uri', Text(2048), nullable=False)
    content = Column('content', Text(30000), nullable=False)
    publ_date = Column('publ_date', Date)
    source = Column('source', String(20))
    miner = Column('miner', String(12))

class TableSources(Base):
    __tablename__ = "tb_sources"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, nullable=False)
    name = Column('name', String(50), nullable=False)

class TableMedia(Base):
    __tablename__ = "tb_media"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableMovements(Base):
    __tablename__ = "tb_movements"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TablePeople(Base):
    __tablename__ = "tb_people"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableEducationalInstitutions(Base):
    __tablename__ = "tb_educ_inst"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('title', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TablePrivateInstitutions(Base):
    __tablename__ = "tb_private_inst"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('title', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TablePublicInstitutions(Base):
    __tablename__ = "tb_public_inst"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('title', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableRacistActions(Base):
    __tablename__ = "tb_racist_actions"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableWorks(Base):
    __tablename__ = "tb_works"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableCities(Base):
    __tablename__ = "tb_cities"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableStates(Base):
    __tablename__ = "tb_states"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableCountries(Base):
    __tablename__ = "tb_countries"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableLaws(Base):
    __tablename__ = "tb_laws"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    title = Column('title', String(50))
    code = Column('code', String(50))
    table_articles = relationship("TableArticles")

class TablePolices(Base):
    __tablename__ = "tb_polices"
    id = Column('id', Integer, primary_key=True)
    hashed_uri = Column('hashed_uri', BigInteger, ForeignKey('tb_articles.hashed_uri'), nullable=False)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")
