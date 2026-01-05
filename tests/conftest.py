import os
from typing import Generator, List

import pytest
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists
from starlette.testclient import TestClient

from src.database import Base, get_db
from src.main import app
from src.routers.conversions import create_conversion
from src.schemas import ConversionCreate


@pytest.fixture
def mock_rates() -> List[dict]:
    return [
        {"code": "USD", "name": "TBD", "rate": 1.035936},
        {"code": "EUR", "name": "TBD", "rate": 1.0},
        {"code": "GBP", "name": "TBD", "rate": 0.834578},
        {"code": "JPY", "name": "TBD", "rate": 158.099455},
        {"code": "INR", "name": "TBD", "rate": 90.706235},
    ]


@pytest.fixture
def another_mock_rates() -> List[dict]:
    return [
        {"code": "HKD", "name": "TBD", "rate": 8.065967},
        {"code": "EUR", "name": "TBD", "rate": 1.0},
        {"code": "CNH", "name": "TBD", "rate": 7.557405},
        {"code": "JPY", "name": "TBD", "rate": 158.099455},
        {"code": "AUD", "name": "TBD", "rate": 1.487268},
    ]


@pytest.fixture
def different_mock_rates() -> List[dict]:
    return [
        {"code": "EUR", "name": "TBD", "rate": 1.0},
        {"code": "USD", "name": "TBD", "rate": 1.035936},
        {"code": "GBP", "name": "TBD", "rate": 0.834578},
        {"code": "AUD", "name": "TBD", "rate": 1.487268},
        {"code": "CNY", "name": "TBD", "rate": 7.553429},
        {"code": "JPY", "name": "TBD", "rate": 158.099455},
    ]


@pytest.fixture(scope="session")
def db_engine() -> Generator[Engine, None, None]:
    db_url = os.getenv("TEST_DATABASE_URL")
    if not db_url:
        raise RuntimeError("TEST_DATABASE_URL environment variable not set")

    engine = create_engine(db_url)
    if not database_exists:
        create_database(engine.url)

    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine: Engine) -> Generator[Session, None, None]:
    connection = db_engine.connect()
    transaction = connection.begin()
    db = Session(bind=connection)
    yield db

    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db) -> Generator[TestClient, None, None]:
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


@pytest.fixture
def conversions(db: Session) -> Session:
    conversion_usd_to_eur = ConversionCreate(
        base_currency="USD", target_currency="EUR", amount=100
    )
    conversion_chf_to_pln = ConversionCreate(
        base_currency="CHF",
        target_currency="PLN",
        amount=74,
    )
    create_conversion(conversion=conversion_usd_to_eur, db=db)
    create_conversion(conversion=conversion_chf_to_pln, db=db)
    return db

@pytest.fixture
def currencies(db: Session) -> Session:
    from src.models import Currency

    currencies = [
        Currency(code="USD", name="United States Dollar", rate=1.035936),
        Currency(code="EUR", name="Euro", rate=1.0),
        Currency(code="GBP", name="British Pound Sterling", rate=0.834578),
        Currency(code="JPY", name="Japanese Yen", rate=158.099455),
        Currency(code="INR", name="Indian Rupee", rate=90.706235),
    ]
    db.add_all(currencies)
    db.commit()
    return db
