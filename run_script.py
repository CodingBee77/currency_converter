from src.currency_converter import convert_currency
from src.utils.rates import get_rates


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get("rates")

    convert_currency(base="EUR", vs="SEK", amount=100, rates=rates)
    convert_currency(base="USD", vs="GBP", amount=50, rates=rates)


if __name__ == "__main__":
    main()
