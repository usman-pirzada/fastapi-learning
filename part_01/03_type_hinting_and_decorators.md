# Python Type Hinting & Function Decorators

---

## 1. What Is Type Hinting?

Type hinting is Python's way of **annotating** what data type a variable, function argument, or return value is expected to be.

```python
def get_shipment(id: int):
    ...
```

- `id: int` → declares that `id` should be an integer
- Python itself **does not enforce** this at runtime by default
- FastAPI **does enforce** it — validation happens automatically

---

## 2. Basic Syntax

```python
# Variable
shipment_id: int = 5

# Function argument
def get_shipment(id: int):
    ...

# Return type
def get_shipment(id: int) -> dict:
    return {"message": "Your shipment is delivered"}
```

---

## 3. Type Hinting in a FastAPI Route

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment/{id}")
def get_shipment(id: int):
    return {"message": "Your shipment is delivered"}
```

Here `id: int` does three things at once:
1. Documents the expected type in Swagger UI
2. Tells FastAPI to parse the incoming URL string as `int`
3. Triggers automatic validation — wrong type → `422` error, no extra code needed

---

## 4. Benefits of Type Hinting in a Web API

| Benefit | What it means |
|---|---|
| ✅ **Automatic Validation** | FastAPI rejects wrong types instantly (`422`) without you writing any validation code |
| ✅ **Auto Documentation** | Swagger UI (`/docs`) reads type hints and shows expected types for every parameter |
| ✅ **Code Readability** | `id: int` is self-documenting — anyone reading the code immediately knows what's expected |
| ✅ **Maintainability** | Easier to refactor confidently when types are explicit throughout the codebase |
| ✅ **Static Analysis** | Tools like **mypy** or **Pyright** catch type mismatches before you even run the code |

---

## 5. Union — Multiple Accepted Types

Use `Union` when a parameter can be **one of several types**.

```python
from typing import Union

def get_user(user_id: Union[int, str]):
    ...
```

Modern Python 3.10+ shorthand (preferred):

```python
def get_user(user_id: int | str):
    ...
```

- Accepts either an `int` or a `str`
- FastAPI will try to parse/validate against each type in order
- Common use case: IDs that can be numeric (`404`) or UUID strings (`"a1b2-c3d4"`)

---

## 6. Optional — May or May Not Be Provided

`Optional[X]` is just shorthand for `Union[X, None]` — it means the value can be the given type **or** `None`.

```python
from typing import Optional

# These two are identical:
def get_shipment(id: Optional[int]):     ...
def get_shipment(id: int | None):        ...
```

To make it truly optional in FastAPI, always pair with `= None`:

```python
def get_shipment(id: int | None = None):
    ...
```

| Declaration | Required? | Accepted Values |
|---|---|---|
| `id: int` | ✅ Yes | integers only |
| `id: int = None` | ❌ No | integers only ⚠️ misleading |
| `id: int \| None = None` | ❌ No | integers or null ✅ |

> Always prefer `int | None = None` over `int = None` — the type hint should truthfully reflect what values are valid.

---

## 7. Tuple and Dict Type Hints

### `tuple`

```python
def get_coords(point: tuple[float, float]) -> tuple[float, float]:
    return point
```

- `tuple[float, float]` → exactly two floats
- `tuple[int, ...]` → a tuple of any number of ints

### `dict`

```python
def process(data: dict[str, int]) -> dict[str, int]:
    ...
```

- `dict[str, int]` → keys are strings, values are integers
- `dict[str, Any]` → keys are strings, values can be anything

### In FastAPI responses

```python
@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, str]:
    return {"status": "delivered", "content": "car"}
```

The return type hint `-> dict[str, str]` tells FastAPI (and Swagger) what shape the response will have.

---

## 8. Decorators — How `@app.get(...)` Works

A **decorator** is a function that wraps another function to extend its behavior without modifying it directly.

### Basic decorator concept

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Equivalent to:
say_hello = my_decorator(say_hello)
```

### FastAPI route decorator

```python
@app.get("/shipment/{id}")
def get_shipment(id: int):
    return {"message": "delivered"}
```

`@app.get("/shipment/{id}")` does the following:
1. Registers the route `/shipment/{id}` with the HTTP method `GET` in FastAPI's internal router
2. Wraps `get_shipment` so FastAPI can intercept calls, parse parameters, validate types, and return responses
3. The function itself stays unchanged — the decorator adds the routing layer on top

> The decorator is evaluated **at import time**, not at request time. Routes are registered when your app starts up.

---

## 9. Route Ordering — Why It Matters

FastAPI matches routes **top to bottom** in the order they are defined. The first match wins.

### ⚠️ Problem — static route shadowed by dynamic route

```python
@app.get("/shipment/{id}")     # ← matches EVERYTHING including "latest"
def get_shipment(id: int):
    ...

@app.get("/shipment/latest")   # ← NEVER reached ❌
def get_latest_shipment():
    ...
```

`GET /shipment/latest` hits the first route and tries to parse `"latest"` as `int` → `422` error.

### ✅ Fix — define specific routes before dynamic ones

```python
@app.get("/shipment/latest")   # ← specific, defined first ✅
def get_latest_shipment():
    ...

@app.get("/shipment/{id}")     # ← dynamic, defined after ✅
def get_shipment(id: int):
    ...
```

**Rule:** Always define **static/specific routes before dynamic `{param}` routes** when their paths would otherwise conflict.

---

## 10. Summary

```
int | str          → Union: accepts either type
int | None = None  → Optional: accepts the type or nothing
tuple[X, Y]        → fixed-structure tuple
dict[str, int]     → typed key-value mapping
@decorator         → wraps a function, registered at startup
Route order        → specific before dynamic, top-to-bottom matching
```