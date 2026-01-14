import os
import sys

import pytest
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, ProgrammingError

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

    try:
        currencies.execute(text("SELECT 1 FROM currencies LIMIT 1"))
    except OperationalError:
        # create tables if missing
        models.Base.metadata.create_all(bind=currencies.bind)

    # Simulate a database error by dropping the currencies table
    currencies.execute(text("DROP TABLE IF EXISTS currencies"))

    # Either the DB exception bubbles up, or the app handles it and returns 500.
    try:
        response = client.get("/currencies")
    except (OperationalError, ProgrammingError):
        # DB exception propagated - test passes
        return

    # If no exception, the app likely caught it and returned an error response
    assert response.status_code == 500
