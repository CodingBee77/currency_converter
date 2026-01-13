import os
import sys

import pytest
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

from src import models

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


load_dotenv()


def test_get_currencies(currencies, client):
    response = client.get("/currencies")
    all_currencies = currencies.query(models.Currency).all()
    all_currencies_json = [cur.to_dict() for cur in all_currencies]

    assert response.status_code == 200
    assert len(response.json()) == 5
    assert response.json() == all_currencies_json


def test_get_currencies_error(currencies, client):
    # Simulate a database error by dropping the currencies table
    currencies.execute(text("DROP TABLE IF EXISTS currencies"))
    with pytest.raises(ProgrammingError):
        response = client.get("/currencies")
        print(response.status_code)
        assert response.status_code == 500
