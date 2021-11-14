from db.credentials import get_session
from db.tables.tb_definitions import TableArticles
from utils import str2date

def add_article(uri, content, publ_date=None, source=None, miner=None, session=None):
    hashed_uri = hash(uri)
    if (not publ_date):
        publ_date = str2date(publ_date)
    article = TableArticles(
                    uri=uri,                    \
                    hashed_uri=hashed_uri,      \
                    content=content,            \
                    publ_date=publ_date,        \
                    source=source,              \
                    miner=miner)
    if (not session):
        session = get_session()
    session.add(article)
    session.commit()
    session.close()
    return
