from src.utils.rates import get_rates


def test_get_rates_mock_true_valid():
    rates = get_rates(mock=True)
    assert rates.get("success") is True
    assert rates.get("timestamp") is not None
    assert rates.get("base") is not None
    assert rates.get("date") is not None
    assert rates.get("rates") is not None


def test_get_rates_valid_api_key():
    rates = get_rates(mock=False)
    assert rates.get("success") is True
    assert rates.get("timestamp") is not None
    assert rates.get("base") is not None
    assert rates.get("date") is not None
    assert rates.get("rates") is not None


def test_get_rates_invalid_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "INVALID_API_KEY")
    rates = get_rates(mock=False)
    print(rates)
    assert "error" in rates
    assert "You have not supplied a valid API Access Key" in rates["error"]["message"]
