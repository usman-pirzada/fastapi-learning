# PUT, PATCH & DELETE (CRUD Operations)

---

## 1. HTTP Methods for Updating Data

| Method | Intent | Scope |
|---|---|---|
| `PUT` | **Replace** the entire resource | All fields |
| `PATCH` | **Modify** specific fields only | Partial fields |
| `DELETE` | **Remove** the resource | Entire resource |

> These are **conventions**, not enforced restrictions. FastAPI won't stop you from using PUT for partial updates — but following these conventions keeps your API predictable and interoperable.

---

## 2. PUT — Full Replacement

### Concept

- Replaces the **entire existing resource** with the new data you provide.
- Fields you **omit** in the request body are either:
  - Reset to their **default value**, or
  - Treated as `null` / removed — depending on how the API is designed.

### URL Structure

```
PUT /shipment/1234
```

### Request Body (JSON)

```json
{
  "content": "car",
  "weight": 200,
  "status": "ordered"
}
```

> All fields must be provided. This is a full replacement of whatever was stored at id `1234`.

### What Happens to Omitted Fields?

- If a field is **required** → API should throw a validation error (e.g., `422`).
- If a field is **optional** → it gets reset to its default or `null`.
- Either way, the **intent** is replacement, not preservation.

---

## 3. PATCH — Partial Modification

### Concept

- Updates **only the fields you provide**.
- All other fields are **left untouched** on the server.
- The server does **not** assume you want to clear or reset anything.

### URL Structure

```
PATCH /shipment/1234
```

### Request Body (JSON)

```json
{
  "status": "delivered"
}
```

> Only `status` is updated. `content` and `weight` remain as-is on the server.

---

## 4. PUT vs PATCH — Side-by-Side

```
Shipment #1234 currently stored:
{ "content": "car", "weight": 200, "status": "ordered" }

After PUT with { "status": "delivered" }:
{ "status": "delivered" }           ← content and weight are gone/reset ⚠️

After PATCH with { "status": "delivered" }:
{ "content": "car", "weight": 200, "status": "delivered" }  ← only status changed ✅
```

---

## 5. DELETE — Remove a Resource

### Concept

- Removes the specified resource from the server entirely.
- The resource is identified via the **URL path** (not the request body).

### URL Structure

```
DELETE /shipment/1234        ← preferred: id as path parameter
DELETE /shipment?id=1234     ← also valid: id as query parameter
```

> `/shipment/{id}` as a path parameter is generally cleaner for resource-specific operations — it reads as "delete the shipment whose ID is 1234."

### Response Body (Optional but Recommended)

```json
{
  "detail": "The shipment with id #1234 deleted successfully!"
}
```

---

## 6. HTTP Status Codes for These Methods

| Scenario | Status Code | Meaning |
|---|---|---|
| Successful PUT / PATCH | `200 OK` | Resource updated, response body returned |
| Successful DELETE (with body) | `200 OK` | Deleted, response body included |
| ✅ Successful DELETE (no body) | `204 No Content` | Deleted, **no response body** |
| Field missing in PUT | `422 Unprocessable Entity` | Validation failed |
| Resource not found | `404 Not Found` | Resource doesn't exist |
| Wrong status code trap | `406 Not Acceptable` | ❌ Content negotiation, NOT deletion |

> **`204 No Content`** is the most precise and conventional response for a successful DELETE where no body is returned. Prefer it over `200` in that case.

---

## 7. `HTTPException` — Only for Errors, Never for Success

### ❌ Common Mistake — Using HTTPException for a Successful DELETE

```python
# WRONG ❌ — contradicts itself
raise HTTPException(
    status_code=status.HTTP_204_NO_CONTENT,
    detail="The shipment with id #1234 deleted successfully!"
)
```

Two problems here:
1. `204 No Content` **must not have a response body** — the status code literally means "no content."
2. `HTTPException` is for **failures**, not successes. A successful delete should `return`, not `raise`.

### ✅ The Correct Mental Model

```
HTTPException  →  Something went wrong / request cannot be fulfilled
return         →  Request succeeded
```

### ✅ Correct Implementation — Option A: 204 No Content (no body)

```python
@app.delete("/shipment/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shipment(id: int) -> None:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!"
        )
    shipments.pop(id)
    # implicit return None → FastAPI sends 204
```

### ✅ Correct Implementation — Option B: 200 OK (with message body)

```python
@app.delete("/shipment/{id}", status_code=status.HTTP_200_OK)
def delete_shipment(id: int) -> dict[str, str]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!"
        )
    shipments.pop(id)
    return {
        "detail": f"The shipment with id #{id} deleted successfully!"
    }
```

---

## 8. Execution Paths & `-> None` Return Type

A function annotated `-> None` can still `raise` exceptions — raising **stops** the function entirely, it does not return anything.

```python
def delete_shipment(id: int) -> None:   # ← "if normal return, it's None"
    if id not in shipments:
        raise HTTPException(...)        # ← function STOPS here, never reaches return
    shipments.pop(id)
    # reaches end → returns None → FastAPI sends 204
```

```
Execution path 1 (success):
  shipments.pop(id) → function ends → return None → 204 No Content

Execution path 2 (error):
  raise HTTPException(...) → function interrupted → FastAPI catches it → 404 + JSON detail
```

> `raise` is an **escape hatch** — it exits the function immediately without returning. The return type annotation only describes the normal completion path.

### Analogy

```python
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")  # ← doesn't violate -> float
    return a / b
```

Same principle — `raise` doesn't break the return type contract because it never reaches `return`.

---

## 9. `detail` in HTTPException — What It Actually Is

`detail` is **not** the function's return value. It is data stored **inside the exception object**.

FastAPI intercepts the raised `HTTPException` and converts `detail` into a JSON response body automatically:

```python
raise HTTPException(
    status_code=404,
    detail="Given id doesn't exist!"
)
```

FastAPI produces:

```json
{
    "detail": "Given id doesn't exist!"
}
```

> `detail` is only meaningful on **error** responses (`4xx`, `5xx`). On `204`, there is no body at all — even if you try to set `detail`, it won't be sent.

---

## 10. DELETE — Full Decision Table

| Situation | Status | Response Body | Mechanism |
|---|---|---|---|
| ✅ Delete succeeded, no message needed | `204 No Content` | ❌ None | `return None` |
| ✅ Delete succeeded + confirmation message | `200 OK` | ✅ JSON | `return {...}` |
| ❌ Shipment doesn't exist | `404 Not Found` | ✅ Error detail | `raise HTTPException(404, ...)` |
| ❌ Invalid request (bad type etc.) | `422` | ✅ Validation error | Auto by FastAPI |

---

## 11. Summary — Decision Guide

```
Need to completely replace a resource?          → PUT   (send all fields)
Need to update just one or two specific fields? → PATCH (send only changed fields)
Need to remove a resource?                      → DELETE (id in URL path preferred)

On success  → return (value or None)
On failure  → raise HTTPException(status_code=4xx, detail="...")

204 + body  → ❌ contradiction, never do this
200 + body  → ✅ valid
204 + None  → ✅ valid
```