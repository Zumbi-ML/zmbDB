from db.credentials import get_engine
from db.tables.tb_definitions import *
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy_utils import database_exists, create_database, drop_database

def drop_n_create_db():
    """
    Drop DB (if existent) and create db schema
    """
    engine = get_engine()
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)
    Base.metadata.create_all(engine)
