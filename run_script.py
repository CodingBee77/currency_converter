from typing import List

from src.currency_converter import convert_currency
from src.utils.rates import get_rates


def main():
    rates = get_rates(mock=False)

    convert_currency(base_currency="EUR", target_currency="SEK", amount=104, rates=rates)
    convert_currency(base_currency="GBP", target_currency="GBP", amount=50, rates=rates)


if __name__ == "__main__":
    main()
