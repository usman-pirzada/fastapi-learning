from fastapi import FastAPI
from typing import Any
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:  # FastAPI will handle the validation for us on this type hinting
    return {
        "id": id,
        "weight": 1.2,
        "content": "wooden table",
        "status": "in transit"
    }

# The order of routes matter. Here, for `/shipment/latest` to work place it before `/shipment/{id}` as the order matters for positional parameters or some set values
@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:  # FastAPI will handle the validation for us on this type hinting
    return {
        "id": 12798,
        "weight": .6,
        "content": "glassware",
        "status": "placed"
    }


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url = app.openapi_url,
        title = "Scalar API"
    )
