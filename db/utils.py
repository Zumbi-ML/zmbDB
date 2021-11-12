from credentials import DB_USER, DB_PWD, DB_HOST, DB_NAME
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine(db_user=DB_USER, db_pwd=DB_PWD, db_host=DB_HOST, db_name=DB_NAME):
    return create_engine(f"mysql://{db_user}:{db_pwd}@{db_host}/{db_name}", echo=True)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
