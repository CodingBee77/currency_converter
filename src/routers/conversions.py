from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src import models
from src import schemas
from src.currency_converter import convert_currency
from src.database import get_db
from src.utils.rates import get_rates

router = APIRouter(prefix="/conversions", tags=["conversions"])


@router.get("/", response_model=List[schemas.Conversion])
def get_conversions(db: Session = Depends(get_db)):
    conversions = db.query(models.Conversion).all()
    return conversions


@router.post(
    "/", response_model=schemas.Conversion, status_code=status.HTTP_201_CREATED
)
def create_conversion(
    conversion: schemas.ConversionCreate, db: Session = Depends(get_db)
):
    mock_rates = get_rates(mock=True)
    try:
        result = convert_currency(
            conversion.base_currency,
            conversion.target_currency,
            conversion.amount,
            mock_rates,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
    new_conversion = models.Conversion(**conversion.dict(), result=result)
    db.add(new_conversion)
    db.commit()
    db.refresh(new_conversion)
    return new_conversion


@router.get(
    "/{conversion_id}",
    response_model=schemas.Conversion,
    status_code=status.HTTP_200_OK,
)
def get_conversion(conversion_id: int, db: Session = Depends(get_db)):
    conversion = (
        db.query(models.Conversion)
        .filter(models.Conversion.id == conversion_id)
        .first()
    )
    if conversion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversion with id {conversion_id} not found",
        )
    return conversion


# TODO: implement soft delete using sql alchemy event listener :
# https://theshubhendra.medium.com/mastering-soft-delete-advanced-sqlalchemy-techniques-4678f4738947
@router.delete("/{conversion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_conversion(conversion_id: int, db: Session = Depends(get_db)):
    conversion = (
        db.query(models.Conversion)
        .filter(models.Conversion.id == conversion_id)
        .first()
    )
    if conversion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conversion with id {conversion_id} not found",
        )
    db.delete(conversion)
    db.commit()
    return {"detail": "Conversion deleted successfully."}
