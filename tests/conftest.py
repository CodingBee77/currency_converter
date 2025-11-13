import pytest


@pytest.fixture
def mock_rates():
    return [
        {"code": "USD", "name": "TBD", "rate": 1.035936},
        {"code": "EUR", "name": "TBD", "rate": 1.0},
        {"code": "GBP", "name": "TBD", "rate": 0.834578},
        {"code": "JPY", "name": "TBD", "rate": 158.099455},
        {"code": "INR", "name": "TBD", "rate": 90.706235}
    ]


@pytest.fixture
def another_mock_rates():
    return [
        {"code": "HKD", "name": "TBD", "rate": 8.065967},
        {"code": "EUR", "name": "TBD", "rate": 1.0},
        {"code": "CNH", "name": "TBD", "rate": 7.557405},
        {"code": "JPY", "name": "TBD", "rate": 158.099455},
        {"code": "AUD", "name": "TBD", "rate": 1.487268}
    ]


@pytest.fixture
def different_mock_rates():
    return [
        {"code": "EUR", "name": "TBD", "rate": 1.0},
        {"code": "USD", "name": "TBD", "rate": 1.035936},
        {"code": "GBP", "name": "TBD", "rate": 0.834578},
        {"code": "AUD", "name": "TBD", "rate": 1.487268},
        {"code": "CNY", "name": "TBD", "rate": 7.553429},
        {"code": "JPY", "name": "TBD", "rate": 158.099455}
    ]

