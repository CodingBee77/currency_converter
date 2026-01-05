from pydantic import BaseModel, ConfigDict, Field


# TODO: Add validation to ensure currency codes are valid ISO 4217 codes.
# TODO: Add validation to ensure exchange rates are positive numbers.
class CurrencyBase(BaseModel):
    """Base schema for currency information."""

    model_config = ConfigDict(from_attributes=True)
    code: str = Field(..., max_length=3, description="Currency code, e.g., 'USD'")
    name: str = Field(
        ...,
        max_length=50,
        description="Full currency name, e.g., 'United States Dollar'",
    )
    rate: float = Field(
        ..., description="Exchange rate relative to a base currency (e.g., EUR)"
    )


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
    """Base schema for currency conversion information."""

    model_config = ConfigDict(from_attributes=True)

    base_currency: str = Field(
        ..., max_length=3, description="Base currency code, e.g., 'EUR'"
    )
    target_currency: str = Field(
        ..., max_length=3, description="Target currency code, e.g., 'USD'"
    )
    amount: float = Field(..., description="Amount to be converted")


class ConversionCreate(ConversionBase):
    """Used when creating a new conversion."""

    pass


class Conversion(ConversionBase):
    """Schema for currency conversion with result included."""

    id: int = Field(..., description="ID of the conversion record")
    result: float = Field(..., description="Result of the conversion")


class ConversionDelete(BaseModel):
    """Used when deleting a conversion record."""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="ID of the conversion record to delete")
