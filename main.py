from src.currency_converter import get_rates, convert_currency


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get("rates")

    convert_currency(100, base="EUR", vs="SEK", rates=rates)


if __name__ == "__main__":
    main()
