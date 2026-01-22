from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()


def scoring(apartment_id: int, surface_area: int) -> int:
    return apartment_id * surface_area


@app.get("/", response_class=FileResponse)
def show_form():
    html_path = Path(__file__).parent / "score.html"
    return FileResponse(html_path)

# I have chosen to implement input validation in a separate function for better code organization.
def validate_inputs(apartment_id: int, surface_area: int) -> None:
    if apartment_id < 0:
        raise HTTPException(status_code=400, detail="apartment_id must be non-negative")
    if surface_area < 0:
        raise HTTPException(status_code=400, detail="surface_area must be non-negative")


@app.get("/score")
def score(apartment_id: int, surface_area: int):
    validate_inputs(apartment_id, surface_area)
    score_value = scoring(apartment_id, surface_area)
    return {
        "apartment_id": apartment_id,
        "surface_area": surface_area,
        "score": score_value,
    }

