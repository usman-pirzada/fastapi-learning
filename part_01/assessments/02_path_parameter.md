# Path Parameter — Assessment

---

## Question 1

**What happens if a FastAPI request sends a string to an endpoint expecting an integer path parameter?**

- ○ The request is processed by treating the string as a wildcard match.
- ○ The request crashes the FastAPI server with a traceback.
- ○ FastAPI converts the string to an integer automatically.
- ✅ The endpoint returns a validation error response.

> **Correct!** FastAPI raises an HTTP `422 Unprocessable Entity` error.

---

## Question 2

**What technique allows a FastAPI application to validate the structure of outgoing responses?**

- ○ Including type comments in API routes
- ○ Implementing FastAPI timer events
- ○ Returning plain dictionaries with keys
- ✅ Utilizing Pydantic models as response models

> **Correct!** Pydantic models can be used to validate response data structures.

---

## Question 3

**How can you combine path and query parameters in a FastAPI function?**

- ○ Only use path parameters in functions
- ○ Query params are not supported in FastAPI
- ○ Use only one kind at a time in FastAPI routes
- ✅ Define both in the function parameters with default values for query parameters

> **Correct!** You specify path and query parameters in the function definition.

---

## Question 4

**How can an endpoint be designed to handle both specific IDs and the term `'latest'` using FastAPI?**

- ○ Set the endpoint to only accept strings and convert internally.
- ○ Allow only `str` in path and check internally whether it is numeric.
- ○ Use separate routes for IDs and `'latest'`.
- ✅ Declare the parameter as `Union[int, str]` to handle both types.

> **Correct!** The `Union` type from the `typing` module allows for multiple types.

---

## Question 5

**In what order does FastAPI execute middleware, dependencies, and route functions during a request?**

- ○ Dependencies → Middleware → Route function
- ○ Dependencies → Route function → Middleware
- ○ Route function → Middleware → Dependencies
- ✅ Middleware → Dependencies → Route function

> **Correct!** This is the right order of execution in FastAPI.

---