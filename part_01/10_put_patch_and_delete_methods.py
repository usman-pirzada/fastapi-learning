from fastapi import FastAPI, HTTPException, status
from typing import Any
import fastapi
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

@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!"
        )
    
    return shipments[id]

@app.post("/shipment")
def add_shipment(content: str, weight: float) -> dict[str, int]:
    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum limit is 25 kg!"
        )
    
    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "weight": weight,
        "content": content,
        "status": "placed"
    }

    return {"id": new_id}

@app.put("/shipment")
def update_shipment(id: int, content: str, weight: float, status: str) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,  # Here writing only status was conflicting with the status attr in fn params
            detail="Given id doesn't exist!"
        )
    
    shipments[id] = {
        "weight": weight,
        "content": content,
        "status": status
    }

    return shipments[id]

# ​We use put method to replace all the fields and patch method when updating a few fields
# These are not restrictions but conventions that should be followed
# This function is not efficient if we have more field as we will be repeating same ifs, see below version
# @app.patch("/shipment")
# def patch_shipment(
#     id: int,
#     content: str | None = None,
#     weight: float | None = None,
#     status: str | None = None,
# ) -> dict[str, Any]:
    
#     shipment = get_shipment(id)

#     if content:
#         shipment["content"] = content
#     if weight:
#         shipment["weight"] = weight
#     if status:
#         shipment["status"] = status

#     shipments[id] = shipment

#     return shipments[id]

@app.patch("/shipment")
def patch_shipment(
    id: int,
    body: dict[str, Any]
) -> dict[str, Any]:
    
    shipment = get_shipment(id)
    shipment.update(body)
    shipments[id] = shipment

    return shipments[id]

@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  # Here writing only status was conflicting with the status attr in fn params
            detail="Given id doesn't exist!"
        )

    shipments.pop(id)

    return {"detail" : f"The shipment with id #{id} deleted successfully!"}



# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs() -> HTMLResponse:
    return get_scalar_api_reference(
        openapi_url = app.openapi_url,
        title = "Scalar API"
    )
