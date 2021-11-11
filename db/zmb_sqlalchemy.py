from sqlalchemy import create_engine

def get_engine(db_user, db_pwd, db_host, db_name):
    return create_engine(f"mysql://{db_user}:{db_pwd}@{db_host}/{db_name}", echo=True)
