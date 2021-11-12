from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TableCollaborators(Base):
    __tablename__ = "tb_collaborators"
    __table_args__ = (UniqueConstraint('cod', name="codx_1"),)
    id = Column('id', Integer, primary_key=True)
    cod = Column('cod', String(12))
    name = Column('name', String(50), nullable=False)
    token = Column('token', String(36), nullable=False)
    perm_level = Column('perm_level', nullable=False)

class TableArticles(Base):
    __tablename__ = "tb_articles"
    __table_args__ = (UniqueConstraint('uri', name="urix_1"),)
    id = Column('id', Integer, primary_key=True)
    miner = Column('miner', String(12), nullable=False)
    publ_date = Column('publ_date', Date)
    uri = Column('uri', String(255), nullable=False)
    source_id = Column('source_id', Integer, ForeignKey('tb_sources.id'), nullable=False)
    table_sources = relationship("TableSources")

class TableSources(Base):
    __tablename__ = "tb_sources"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), nullable=False)

class TableMedia(Base):
    __tablename__ = "tb_media"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableMovements(Base):
    __tablename__ = "tb_movements"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TablePeople(Base):
    __tablename__ = "tb_people"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableEducationalInstitutions(Base):
    __tablename__ = "tb_educ_inst"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('title', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TablePrivateInstitutions(Base):
    __tablename__ = "tb_private_inst"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('title', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TablePublicInstitutions(Base):
    __tablename__ = "tb_public_inst"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('title', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableRacistActions(Base):
    __tablename__ = "tb_racist_actions"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableWorks(Base):
    __tablename__ = "tb_works"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableCities(Base):
    __tablename__ = "tb_cities"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableStates(Base):
    __tablename__ = "tb_states"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableCountries(Base):
    __tablename__ = "tb_countries"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    name = Column('name', String(50), nullable=False)
    table_articles = relationship("TableArticles")

class TableLaws(Base):
    __tablename__ = "tb_laws"
    id = Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True)
    title = Column('title', String(50))
    code = Column('code', String(50))
    table_articles = relationship("TableArticles")
