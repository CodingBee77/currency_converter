import json
import os
from typing import Final, List

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL: Final[str] = os.environ.get("BASE_URL")
API_URL: Final[str] = os.environ.get("API_URL")


def get_rates(mock: bool = False) -> List[dict]:
    rates_path = os.path.join(os.path.dirname(__file__), "rates_DB.json")
    if mock:
        with open(rates_path, "r") as file:
            rates_response = json.load(file)
            return rates_response

    # TODO: Change to actual external API call in the future
    rates_response = requests.get(f"{API_URL}/currencies/").json()
    return rates_response
