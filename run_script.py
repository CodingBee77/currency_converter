from src.currency_converter import convert_currency
from src.utils.rates import get_rates


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get("rates")

    convert_currency(base_currency="EUR", target_currency="SEK", amount=100, rates=rates)
    convert_currency(base_currency="USD", target_currency="GBP", amount=50, rates=rates)


if __name__ == "__main__":
    main()
