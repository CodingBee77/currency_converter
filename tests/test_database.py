import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.database import get_db
from src.main import app


load_dotenv()

engine = create_engine(os.environ.get("TEST_DATABASE_URL"))
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    connection = engine.connect()

    # begin a non-ORM transaction
    transaction = connection.begin()

    # bind an individual Session to the connection
    db = Session(bind=connection)

    yield db

    db.close()
    transaction.rollback()
    connection.close()

app.dependency_overrides[get_db] = override_get_db