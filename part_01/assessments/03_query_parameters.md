# Query Parameter — Assessment

---

## Question 1

**How can you create routes in FastAPI that use both path and query parameters?**

- ○ Only one parameter type can be used per route.
- ○ You must encode path parameters within query strings.
- ○ You must choose only query parameters for efficiency.
- ✅ Path parameters are defined first, followed by query parameters in the function definition.

> **Correct!** You define path parameters as part of the route itself and query parameters as additional arguments.

---

## Question 2

**Which HTTP status code is typically used for client-side errors when an invalid ID is accessed?**

- ○ `500 Internal Server Error`
- ○ `200 OK`
- ○ `301 Moved Permanently`
- ✅ `404 Not Found`

> **Correct!** `404 Not Found` is used when a client attempts to access a non-existent resource.

---

## Question 3

**What FastAPI feature can help validate query parameters like `id` in your route?**

- ○ Environment variables for configuration.
- ○ Using Python comments for notes.
- ○ Validation is handled by the server defaults.
- ✅ Type annotations in the route handler function parameters.

> **Correct!** FastAPI uses type annotations to perform input validation, including query parameters.

---

## Question 4

**What is a primary benefit of creating a route to access specific fields of an entity in FastAPI?**

- ○ It provides no significant benefit.
- ○ It simplifies logging.
- ○ It completely secures the data.
- ✅ It allows for more controlled and efficient data retrieval.

> **Correct!** Specifying fields lets clients request only necessary data, improving efficiency.

---

## Question 5

**What does the POST method typically handle in FastAPI routes?**

- ○ Deleting existing data.
- ○ Updating existing data entries.
- ○ Fetching data based on a parameter.
- ✅ Creating new resources or data entries.

> **Correct!** The POST method is commonly used to add new entries to a data source.

---