def get_currency(currency: str, rates: dict) -> float:
    currency = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f"'{currency}' is not a valid currency.")


# TODO: unify arguments with schemas.ConversionBase
def convert_currency(base: str, vs: str, amount: float, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f"{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})")
    return conversion
