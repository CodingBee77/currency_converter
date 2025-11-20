from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src import models
from src.main import app

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

client = TestClient(app)

load_dotenv()
engine = create_engine(os.environ.get("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_get_conversions():
    response = client.get("/conversions")
    db = next(get_db())
    all_conversions = db.query(models.Conversion).all()
    all_conversions_json = [conversion.to_dict() for conversion in all_conversions]
    assert response.status_code == 200
    assert response.json() == all_conversions_json


def test_post_conversion():
    conversion_data = {
        "base_currency": "USD",
        "target_currency": "EUR",
        "amount": 50
    }
    response = client.post("/conversions/", json=conversion_data)
    assert response.status_code == 201
    data = response.json()
    assert data["base_currency"] == "USD"
    assert data["target_currency"] == "EUR"
    assert data["amount"] == 50
    assert "id" in data
    assert "result" in data


def test_post_conversion_invalid_currency():
    conversion_data = {
        "base_currency": "XXX",  # Invalid currency code
        "target_currency": "EUR",
        "amount": 50
    }
    response = client.post("/conversions/", json=conversion_data)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "'XXX' is not a valid currency."


def test_post_conversion_invalid_amount():
    conversion_data = {
        "base_currency": "USD",
        "target_currency": "EUR",
        "amount": -10  # Invalid amount
    }
    response = client.post("/conversions/", json=conversion_data)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Amount must be greater than zero."


def test_post_conversion_missing_field():
    conversion_data = {
        "base_currency": "USD",
        # "target_currency" is missing
        "amount": 50
    }
    response = client.post("/conversions/", json=conversion_data)
    assert response.status_code == 422  # Unprocessable Entity
    data = response.json()
    assert data["detail"][0]["loc"] == ["body", "target_currency"]
    assert data["detail"][0]["msg"] == "Field required"


def test_get_conversion_by_id():
    conversion_id = 1
    response = client.get(f"/conversions/{conversion_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == conversion_id
    assert data["base_currency"] == "EUR"
    assert data["target_currency"] == "GBP"
    assert data["amount"] == 10
    assert data["result"] == 8.35


def test_get_conversion_not_found():
    conversion_id = 9999  # Assuming this ID does not exist
    response = client.get(f"/conversions/{conversion_id}")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == f"Conversion with id {conversion_id} not found"
