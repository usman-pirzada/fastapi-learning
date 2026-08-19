from fastapi import FastAPI, HTTPException, status
from typing import Any, Literal
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!"
        )
    
    return shipments[id]

# @app.post("/shipment")
# def add_shipment(content: str, weight: float) -> dict[str, int]:
#     new_id = max(shipments.keys()) + 1

#     shipments[new_id] = {
#         "weight": weight,
#         "content": content,
#         "status": "placed"
#     }

#     return {"id": new_id}

# @app.post("/shipment")
# def add_shipment(weight: float, data: dict[str, str]) -> dict[str, int]:
#     content = data["content"]

#     new_id = max(shipments.keys()) + 1

#     shipments[new_id] = {
#         "weight": weight,
#         "content": content,
#         "status": "placed"
#     }

#     return {"id": new_id}

@app.post("/shipment")
# Even if function is written like this, the client can still send query params in the URL, like ?weight=2.5&content=hp along with JSON in the body, like {"weight": 3, "content": "hp elitebook"}. FastAPI will only pass what matches the function signature.
# Pydantic Model can be used for more validation here
def add_shipment(data: dict[str, Any]) -> dict[str, int]:
    weight = data["weight"]
    content = data["content"]

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "weight": weight,
        "content": content
    }

    return {"id": new_id}


# Its just a demo of how we can mix ​and match the query and path parameters
# Specific-field route:
# Use a path parameter to choose which field of a shipment to retrieve,
# and a query parameter to identify the shipment.
# Example: GET /shipment/status?id=893764 → {"status": "placed"}
# This demonstrates controlled retrieval of a specific entity field
# instead of returning the entire shipment object.
@app.get("/shipment/{field}")
def get_shipment_field(field: Literal["content", "weight", "status"], id: int) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!"
        )

    # return shipments[id][field]   # can be returned like this, but NOT recommended
    return {
        field: shipments[id][field]
    }



# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs() -> HTMLResponse:
    return get_scalar_api_reference(
        openapi_url = app.openapi_url,
        title = "Scalar API"
    )
