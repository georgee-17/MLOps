from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/{surface_area}")
def read_item(surface_area: int, name: str, price: float):
    if surface_area < 0:
        raise HTTPException(status_code=400, detail="Surface area cannot be negative")
    if price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    
    return {
        "surface_area": surface_area,
        "name": name,
        "price_euros": price
    }