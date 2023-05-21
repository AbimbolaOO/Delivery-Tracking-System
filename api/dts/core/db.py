import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)
Base.query = db_session.query_property()


def init_db():
    import dts.models.v1

    Base.metadata.create_all(bind=engine)
