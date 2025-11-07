import json
import os
from typing import Final

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL: Final[str] = os.environ.get("BASE_URL")


def get_rates(mock: bool = False) -> dict:
    rates_path = os.path.join(os.path.dirname(__file__), "rates.json")
    if mock:
        with open(rates_path, "r") as file:
            rates_response = json.load(file)
            return rates_response.get("rates")

    # TODO: Remove it and use rates from database
    # Fetch API_KEY dynamically at runtime
    api_key = os.environ.get("API_KEY")
    payload: dict = {"access_key": api_key}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data
