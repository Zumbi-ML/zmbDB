import os
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, ForeignKey, select, UniqueConstraint
from credentials import DB_USER, DB_PWD, DB_HOST, DB_NAME
from db.zmb_sqlalchemy import get_engine

def create_db():
    drop_db_stmt = f"""drop database if exists {DB_NAME};"""
    create_db_stmt = f"""create database {DB_NAME} character set utf8mb4 collate utf8mb4_unicode_ci;"""
    os.system(f"""mysql -u{DB_USER} -p{DB_PWD} < db/sql/create-db.sql""")

def create_schema():
    meta = MetaData()

    tb_collaborators = Table('tb_collaborators', meta,
        Column('id', Integer, primary_key=True),        \
        Column('cod', String(50), nullable=False),      \
        Column('name', String(50), nullable=False),     \
        UniqueConstraint('cod', name="codx_1"),)

    tb_people = Table('tb_people', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_movements = Table('tb_movements', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_cities = Table('tb_cities', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_states = Table('tb_states', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_countries = Table('tb_countries', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_works = Table('tb_works', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_sources = Table('tb_sources', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_media = Table('tb_media', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),        \
                Column('name', String(50), nullable=False),)

    tb_laws = Table('tb_laws', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),       \
                Column('name', String(50), nullable=False),                             \
                Column('code', String(10), nullable=False),)

    tb_educational = Table('tb_educational', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),       \
                Column('name', String(50), nullable=False),)

    tb_public = Table('tb_public', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),       \
                Column('name', String(50), nullable=False),)

    tb_private = Table('tb_private', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),       \
                Column('name', String(50), nullable=False),)

    tb_actions = Table('tb_actions', meta,
                Column('id', Integer, ForeignKey('tb_uri.id'), primary_key=True),       \
                Column('name', String(50), nullable=False),)

    tb_uri = Table('tb_uri', meta,                              \
                Column('id', Integer, primary_key=True),        \
                Column('miner', String(10)),                    \
                Column('uri', String(300), nullable=False),     \
                Column('media_id', Integer, ForeignKey('tb_media.id'), nullable=False),     \
                UniqueConstraint('uri', name="idx_1"),)

    engine = get_engine(DB_USER, DB_PWD, DB_HOST, DB_NAME)
    meta.create_all(engine)

def main():
    create_db()
    create_schema()

main()
