# Query Parameters

---

## 1. What Are Query Parameters?

Query parameters are another way to pass data to a route handler — the alternative to **path parameters**.

| Feature | Path Parameter | Query Parameter |
|---|---|---|
| Location in URL | Embedded in the path | After a `?` at the end |
| Syntax example | `/shipment/3` | `/shipment?id=3` |
| Defined in code as | `{id}` in the route decorator | Regular function argument (no `{}`) |

---

## 2. URL Syntax

```
/shipment?id=3
  ↑       ↑   ↑
 route  ?name=value
```

- `?` → signals the start of query parameters
- `name=value` → the parameter and its value
- Multiple query params use `&`:  `/shipment?id=3&status=active`

---

## 3. Defining Query Parameters in FastAPI

FastAPI's **default behavior**: any function argument that is **not** a path parameter (i.e., not wrapped in `{}` in the decorator) is automatically treated as a query parameter.

```python
@app.get("/shipment")
def get_shipment(id: int):
    return shipments[id]
```

> `id` is not in `/shipment`, so FastAPI reads it from `?id=...` in the URL automatically.

---

## 4. Validation (Same as Path Parameters)

Query parameters get **the same automatic validation** as path parameters — for free.

```
GET /shipment?id=hello    →  422 Unprocessable Entity (string, not int)
GET /shipment?id=3.5      →  422 Unprocessable Entity (float, not int)
GET /shipment?id=3        →  200 OK ✅
```

FastAPI uses the type hint (`int`, `str`, `float`, etc.) to validate and parse the incoming value automatically.

---

## 5. Required vs Optional Query Parameters

### 5.1 Required (Default Behavior)

```python
@app.get("/shipment")
def get_shipment(id: int):
    return shipments[id]
```

- `id` has **no default value** → it is **required**
- Omitting it: `GET /shipment` → `422: field required`
- Docs (Swagger UI) will mark it as **required**

---

### 5.2 Making It Optional — Two Ways

#### ✅ Preferred Way (Explicit `int | None` with `= None`)

```python
from typing import Optional

@app.get("/shipment")
def get_shipment(id: int | None = None):
    ...
```

- Type is `int | None` → FastAPI documents it as **integer or null**
- Default is `None` → parameter is **not required**
- Swagger UI shows: `integer | null`, not required ✅

#### ⚠️ Not Preferred (Just `= None`, no `None` in type)

```python
@app.get("/shipment")
def get_shipment(id: int = None):
    ...
```

- Works at runtime, but type hint says `int` while default is `None`
- Swagger UI shows: `integer`, not required — **misleading**, because `null` is actually valid
- Inconsistent: the type hint lies about what values are accepted

> **Rule:** Always match your type hint with your actual accepted values.
> If `None` is a valid value, include `None` in the type hint.

---

## 6. Fallback Logic When Parameter Is Absent

A common pattern: if the optional query param is not provided, fall back to a sensible default at the **application level**.

```python
@app.get("/shipment")
def get_shipment(id: int | None = None):
    if not id:
        # Fallback: return the latest shipment
        id = max(shipments.keys())
    return shipments[id]
```

- `GET /shipment`      → returns latest shipment (max key)
- `GET /shipment?id=2` → returns shipment with id=2

This is a **business logic fallback**, not a FastAPI feature — you write it yourself inside the handler.

---

## 7. Auto-Generated Documentation

FastAPI auto-generates Swagger UI docs at `/docs`. Query parameters are clearly shown there:

| Scenario | Shown in Docs |
|---|---|
| `id: int` | Required, type: integer |
| `id: int \| None = None` | Not required, type: integer \| null ✅ |
| `id: int = None` | Not required, type: integer ⚠️ (misleading) |

---

## 8. Summary — Key Takeaways

```
1. Query params → defined after `?` in URL as name=value pairs
2. FastAPI detects them automatically — any arg not in the route path is a query param
3. Full validation applies (wrong type → 422 error)
4. Required by default if no default value is set
5. Make optional with: id: int | None = None  ← preferred
6. Do NOT use: id: int = None               ← misleading type hint
7. You can add fallback logic inside the handler for absent optional params
```