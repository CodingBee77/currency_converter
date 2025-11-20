from typing import List


def get_currency(currency: str, rates: List[dict]) -> float:
    currency = currency.upper()
    currency_rate = next((rate for rate in rates if rate["code"] == currency), None)

    if currency_rate:
        return currency_rate["rate"]
    else:
        raise ValueError(f"'{currency}' is not a valid currency.")


def convert_currency(base_currency: str, target_currency: str, amount: float, rates: List[dict]) -> float:
    base_rate = get_currency(base_currency, rates)
    target_rate = get_currency(target_currency, rates)
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    conversion: float = round((target_rate / base_rate) * amount, 2)
    print(f"{amount:,.2f} ({base_currency}) is: {conversion:,.2f} ({target_currency})")
    return conversion
