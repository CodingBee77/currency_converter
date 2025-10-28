import pytest

from src.currency_converter import convert_currency, get_currency


def test_get_currency_valid(mock_rates):
    assert get_currency("USD", mock_rates) == 1.035936
    assert get_currency("eur", mock_rates) == 1
    assert get_currency("JPY", mock_rates) == 158.099455


def test_get_currency_value_error(another_mock_rates):
    with pytest.raises(ValueError, match="'ABC' is not a valid currency."):
        get_currency("ABC", another_mock_rates)


def test_convert_currency_valid(mock_rates):
    result = convert_currency(100, "USD", "EUR", mock_rates)
    assert result == pytest.approx(96.54, 0.01)  # 100 * (1 / 1.035936)

    result = convert_currency(200, "GBP", "JPY", mock_rates)
    assert result == pytest.approx(37857.89, 0.01)  # 200 * (158.099455 / 0.834578)


def test_convert_currency_invalid_base_value_error(different_mock_rates):
    with pytest.raises(ValueError, match="'ABC' is not a valid currency."):
        convert_currency(100, "ABC", "USD", different_mock_rates)


def test_convert_currency_invalid_vs_value_error(different_mock_rates):
    with pytest.raises(ValueError, match="'XYZ' is not a valid currency."):
        convert_currency(100, "USD", "XYZ", different_mock_rates)
