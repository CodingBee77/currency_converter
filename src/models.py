from database import Base
from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, text


class Currency(Base):
    __tablename__ = "currencies"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(3), unique=True, nullable=False)  # e.g. "USD"
    name = Column(String(50), nullable=False)  # e.g. "United States Dollar"
    rate = Column(Float, nullable=False)  # Exchange rate relative to a base currency (e.g., EUR)


class Conversion(Base):
    __tablename__ = "conversions"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    base_currency = Column(String(3), nullable=False)  # e.g. "EUR"
    target_currency = Column(String(3), nullable=False)
    amount = Column(Float, nullable=False)
    result = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
