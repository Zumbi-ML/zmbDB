import pytest
from utils import get_property
from sqlalchemy_utils import database_exists, create_database, drop_database
from db.tables.tb_definitions import *

@pytest.mark.order(1)
def test_if_db_url(session):
    """
    Test whether a database URL is valid
    """
    DB_USER = get_property("db_user")
    DB_PWD = get_property("db_pwd")
    DB_HOST = get_property("db_host")
    DB_NAME = get_property("db_name")

    db_url = f"mysql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}_test"

    assert str(session.get_bind().url) == db_url

@pytest.mark.order(2)
def test_drop_db(session):
    """
    Test whether a database can be dropped for the tests
    """
    engine_url = session.get_bind().url
    drop_database(engine_url)
    assert database_exists(engine_url) == False

@pytest.mark.order(3)
def test_create_db(session):
    """
    Test whether a database can be created for the tests
    """
    engine_url = session.get_bind().url
    create_database(engine_url)
    assert database_exists(engine_url) == True

@pytest.mark.order(4)
def test_create_db_schema(session):
    """
    Test the creation of the DB schema
    """
    engine = session.get_bind()
    Base.metadata.create_all(engine)
