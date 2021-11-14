from db.credentials import get_engine
from db.tables.tb_definitions import *
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy_utils import database_exists, create_database, drop_database

engine = get_engine()

def create_db():
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

def create_tables():
    Base.metadata.create_all(engine)

def recreate():
    create_db()
    create_tables()

recreate()
