from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy_utils import database_exists, create_database, drop_database
from tables.tb_definitions import *
from utils import get_engine

engine = get_engine()

def create_db():
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

def create_schema():
    Base.metadata.create_all(engine)

def execute():
    create_db()
    create_schema()

execute()
