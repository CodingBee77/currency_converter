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


@app.get("/rates")
async def get_rates(mock: bool = True) -> dict:
    """
    Endpoint to get all available rates.
    """
    if mock:
        with open("rates.json", "r") as file:
            return json.load(file)

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    return data


@app.get("/rates/single_rate")
async def get_single_rate(currency: str):
    """
    Endpoint to get a single rate for a specific currency.
    Requires a query parameter `currency` to specify which currency rate to fetch.
    Example: /rates/single_rate?currency=USD
    """
    rate = rates_data.get(currency.upper())
    if rate is None:
        return {"error": "Currency not found"}
    return {currency.upper(): rate}


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()
