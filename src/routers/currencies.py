from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import models, schemas
from database import get_db

router = APIRouter(prefix="/currencies", tags=["currencies"])


@router.get("/", response_model=List[schemas.CurrencyBase])
def get_currencies(db: Session = Depends(get_db)):
    currencies = db.query(models.Currency).all()
    return currencies


@router.get(
    "/{code}", response_model=schemas.CurrencyBase, status_code=status.HTTP_200_OK
)
def get_currency_by_code(code: str, db: Session = Depends(get_db)):
    currency = db.query(models.Currency).filter(models.Currency.code == code).first()
    if currency is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Currency with code {code} not found",
        )
    return currency
