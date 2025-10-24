import json
from typing import Final
import requests


# TODO: load from .env file
BASE_URL: Final[str] = "https://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = "dbe0b5484149bfb2a16a2cfd1853ae4f"


def get_rates(mock: bool = False) -> dict:
    if mock:
        with open("rates.json", "r") as file:
            return json.load(file)

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data
