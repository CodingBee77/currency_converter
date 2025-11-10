def get_currency(currency: str, rates: dict) -> float:
    currency = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f"'{currency}' is not a valid currency.")


def convert_currency(base_currency: str, target_currency: str, amount: float, rates: dict) -> float:
    base_rate: float = get_currency(base_currency, rates)
    vs_rate: float = get_currency(target_currency, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f"{amount:,.2f} ({base_currency}) is: {conversion:,.2f} ({target_currency})")
    return conversion
