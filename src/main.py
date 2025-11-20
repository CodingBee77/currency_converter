from fastapi import FastAPI

from src import models
from src.database import engine
from src.routers import conversions, currencies

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(conversions.router)
app.include_router(currencies.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
