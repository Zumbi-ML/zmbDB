from utils import get_property
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = get_property("db_user")
DB_PWD = get_property("db_pwd")
DB_HOST = get_property("db_host")
DB_NAME = get_property("db_name")
DB_DEBUG_MODE = get_property("db_debug_mode") == "True"

def get_engine(db_user=DB_USER, db_pwd=DB_PWD, db_host=DB_HOST, db_name=DB_NAME):
    return create_engine(f"mysql://{db_user}:{db_pwd}@{db_host}/{db_name}", echo=DB_DEBUG_MODE)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
