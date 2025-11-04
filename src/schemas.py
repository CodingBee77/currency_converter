from pydantic import BaseModel, Field


class CurrencyBase(BaseModel):
    code: str = Field(..., max_length=3, description="Currency code, e.g., 'USD'")
    name: str = Field(
        ...,
        max_length=50,
        description="Full currency name, e.g., 'United States Dollar'",
    )
    rate: float = Field(
        ..., description="Exchange rate relative to a base currency (e.g., EUR)"
    )

    class Config:
        from_attributes = True


class CurrencyCreate(CurrencyBase):
    """Used when creating a new currency."""

    pass


class CurrencyUpdate(BaseModel):
    """Used when updating a currency (partial update allowed)."""

    id: int = Field(..., description="ID of the currency to update")
    code: str | None = Field(
        None, max_length=3, description="Currency code, e.g., 'USD'"
    )
    name: str | None = Field(
        None,
        max_length=50,
        description="Full currency name, e.g., 'United States Dollar'",
    )
    rate: float | None = Field(
        None, description="Exchange rate relative to a base currency (e.g., EUR)"
    )


class ConversionBase(BaseModel):
    base_currency: str = Field(
        ..., max_length=3, description="Base currency code, e.g., 'EUR'"
    )
    target_currency: str = Field(
        ..., max_length=3, description="Target currency code, e.g., 'USD'"
    )
    amount: float = Field(..., description="Amount to be converted")

    class Config:
        from_attributes = True


class ConversionCreate(ConversionBase):
    pass


class Conversion(ConversionBase):
    result: float = Field(..., description="Result of the conversion")


class ConversionDelete(BaseModel):
    id: int = Field(..., description="ID of the conversion record to delete")

    class Config:
        from_attributes = True
