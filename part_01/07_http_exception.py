from http.client import NOT_FOUND

from fastapi import FastAPI, HTTPException, status
from typing import Any
from scalar_fastapi import get_scalar_api_reference
from starlette.responses import HTMLResponse

app = FastAPI()

shipments = {
    893764: {
        "weight": .6,
        "content": "glassware",
        "status": "placed"
    },
    893765: {
        "weight": 1.2,
        "content": "wooden table",
        "status": "in transit"
    },
    893766: {
        "weight": 0.8,
        "content": "ceramic bowls",
        "status": "placed"
    },
    893767: {
        "weight": 2.4,
        "content": "office chair",
        "status": "shipped"
    },
    893768: {
        "weight": 0.3,
        "content": "books",
        "status": "delivered"
    },
    893769: {
        "weight": 5.7,
        "content": "metal cabinet",
        "status": "in transit"
    },
    893770: {
        "weight": 1.0,
        "content": "lamp",
        "status": "placed"
    }
}

@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]

@app.get("/shipment")
def get_shipment(id: int | None = None) -> dict[str, Any]:  # This can also be done but NOT preferred: def get_shipment(id: int = None) -> dict[str, Any]:
    if not id:
        return get_latest_shipment()

    if id not in shipments:
        raise HTTPException(
            # status_code=404,    # It is also valid
            # status_code=NOT_FOUND,    # It is also valid
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!"
        )
    
    return shipments[id]


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs() -> HTMLResponse:
    return get_scalar_api_reference(
        openapi_url = app.openapi_url,
        title = "Scalar API"
    )
