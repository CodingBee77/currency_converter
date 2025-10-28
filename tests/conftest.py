import pytest


@pytest.fixture
def mock_rates():
    return {
        "USD": 1.035936,
        "EUR": 1.0,
        "GBP": 0.834578,
        "JPY": 158.099455,
        "INR": 90.706235,
    }


@pytest.fixture
def another_mock_rates():
    return {
        "EUR": 1.0,
        "USD": 1.035936,
        "GBP": 0.834578,
        "JPY": 158.099455,
        "AUD": 1.487268,
    }


@pytest.fixture
def different_mock_rates():
    return {
        "EUR": 1.0,
        "USD": 1.035936,
        "GBP": 0.834578,
        "JPY": 158.099455,
        "CNY": 7.553429,
    }
