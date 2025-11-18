import pytest
import requests.exceptions

from src.utils.rates import get_rates
import random


def test_get_rates_mock_true_valid():
    rates = get_rates(mock=True)
    index = random.randrange(0, len(rates))
    assert isinstance(rates, list)
    assert isinstance(rates[index].get("code"), str)
    assert isinstance(rates[index].get("name"), str)
    assert isinstance(rates[index].get("rate"), float)
    assert len(rates[index]) == 3


@pytest.mark.skipif(
    True,
    reason="Skipping test to avoid external API call during testing. "
    "Uncomment this decorator to run the test when the API is available.")
def test_get_rates_mock_is_false():
    rates = get_rates(mock=False)
    index = random.randrange(0, len(rates))
    assert isinstance(rates, list)
    assert isinstance(rates[index].get("code"), str)
    assert isinstance(rates[index].get("name"), str)
    assert isinstance(rates[index].get("rate"), float)
    assert len(rates[0]) == 3


def test_get_rates_mock_is_false_no_response():
    with pytest.raises(requests.exceptions.ConnectionError):
        rates = get_rates(mock=False)
