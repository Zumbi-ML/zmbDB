from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy_utils import database_exists, create_database, drop_database

from credentials import DB_USER, DB_PWD, DB_HOST, DB_NAME
from zmb_sqlalchemy import get_engine

engine = get_engine(DB_USER, DB_PWD, DB_HOST, DB_NAME)

def create_db():
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

def create_schema():
    meta = MetaData()

    Table('tb_collaborators', meta,
        Column('id', Integer, primary_key=True),                                      \
        Column('cod', String(50), nullable=False),                                    \
        Column('name', String(50), nullable=False),                                   \
        UniqueConstraint('cod', name="codx_1"),)

    Table('tb_people', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),        \
        Column('name', String(50), nullable=False),)

    Table('tb_movements', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),        \
        Column('name', String(50), nullable=False),)

    Table('tb_cities', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),        \
        Column('name', String(50), nullable=False),)

    Table('tb_states', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),        \
        Column('name', String(50), nullable=False),)

    Table('tb_countries', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),        \
        Column('name', String(50), nullable=False),)

    Table('tb_works', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),        \
        Column('name', String(50), nullable=False),)

    Table('tb_sources', meta,
        Column('id', Integer, primary_key=True),                                      \
        Column('name', String(50), nullable=False),)

    Table('tb_media', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),        \
        Column('name', String(50), nullable=False),)

    Table('tb_laws', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),       \
        Column('name', String(50), nullable=False),                                  \
        Column('code', String(10), nullable=False),)

    Table('tb_educ_inst', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),       \
        Column('name', String(50), nullable=False),)

    Table('tb_public_inst', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),       \
        Column('name', String(50), nullable=False),)

    Table('tb_private_inst', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),       \
        Column('name', String(50), nullable=False),)

    Table('tb_actions', meta,
        Column('id', Integer, ForeignKey('tb_articles.id'), primary_key=True),       \
        Column('name', String(50), nullable=False),)

    Table('tb_articles', meta,                                                      \
        Column('id', Integer, primary_key=True),                                    \
        Column('miner', String(10)),                                                \
        Column('publ_date', Date),                                                  \
        Column('uri', String(300), nullable=False),                                 \
        Column('source_id', Integer, ForeignKey('tb_media.id'), nullable=False),    \
        UniqueConstraint('uri', name="idx_1"),)

    meta.create_all(engine)

def main():
    create_db()
    create_schema()

main()
