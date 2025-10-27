from src.currency_converter import convert_currency
from src.utils.rates import get_rates


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get("rates")

    convert_currency(100, base="EUR", vs="SEK", rates=rates)
    convert_currency(50, base="USD", vs="GBP", rates=rates)


if __name__ == "__main__":
    main()
