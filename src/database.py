import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
engine = create_engine(os.environ.get("DATABASE_URL"))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# TODO: change to async session if needed
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
