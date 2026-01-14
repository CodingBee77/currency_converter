from datetime import datetime

from sqlalchemy import (Column, DateTime, Float, Integer, String,
                        text)

from src.database import Base


class Currency(Base):
    __tablename__ = "currencies"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(3), unique=True, nullable=False)  # e.g. "USD"
    name = Column(String(50), nullable=False)  # e.g. "United States Dollar"
    rate = Column(
        Float, nullable=False
    )  # Exchange rate relative to a base currency (e.g., EUR)

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "rate": self.rate,
        }


class Conversion(Base):
    __tablename__ = "conversions"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    base_currency = Column(String(3), nullable=False)  # e.g. "EUR"
    target_currency = Column(String(3), nullable=False)
    amount = Column(Float, nullable=False)
    result = Column(Float, nullable=False)
    timestamp = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    def to_dict(self):
        return {
            "id": self.id,
            "base_currency": self.base_currency,
            "target_currency": self.target_currency,
            "amount": self.amount,
            "result": self.result,
        }
