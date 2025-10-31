from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'jdbc:postgresql://localhost:5432/currency_converter'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#TODO: change to async in the future
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
