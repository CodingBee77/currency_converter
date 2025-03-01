import json
from fastapi import APIRouter

from core.config import INPUT_EXAMPLE
from services.predict import MachineLearningModelHandlerScore as model
from models.rates import (
    Rates,
    SingleRate
)

router = APIRouter()

from fastapi import FastAPI

from api.routes.api import router as api_router
from core.events import create_start_app_handler
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION

import json
import os
from typing import Final

import requests
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

load_dotenv()
API_KEY: Final[str] = os.getenv("API_KEY")
BASE_URL: Final[str] = os.getenv("BASE_URL")


def get_mock_rates() -> dict:
    #TODO: define path to the mock data - otherwise use current directory
    with open("rates.json", "r") as file:
        return json.load(file)


@app.get("/rates", response_model=Rates, name="rates:get-all-rates")
async def get_rates(mock: bool = True):
    """
    Endpoint to get all available rates.
    """
    if mock:
        # TODO: extract to separate function
        return get_mock_rates()

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data


# TODO: Create pydantic models
@app.get("/rates/single_rate", response_model=SingleRate, name="rates:get-single-rate")
async def get_single_rate(currency: str):
    """
    Endpoint to get a single rate for a specific currency.
    Requires a query parameter `currency` to specify which currency rate to fetch.
    Example: /rates/single_rate?currency=USD
    """
    rates_data = get_mock_rates()
    rate = rates_data.get(currency.upper())
    if rate is None:
        # TODO: Create custom error
        return {"error": "Currency not found"}
    return {currency.upper(): rate}
