# CRUD Operations — Assessments

---

## Question 1

**What should the response body contain when an API resource is successfully deleted?**

- ○ Error details
- ○ Unchanged resource data
- ○ The deleted resource data
- ✅ A confirmation message or status

> **Correct!** A confirmation message or status code is usually returned, but often with no body.

---

## Question 2

**Why is it crucial to thoroughly test RESTful API endpoints before deployment?**

- ○ To prevent competitors from understanding the API structure
- ○ To make the API slower, allowing for bandwidth management
- ○ To ensure endpoints are not used excessively
- ✅ To identify and fix bugs, ensuring reliable performance

> **Correct!** Testing discovers and resolves issues to maintain performance and reliability.

---

## Question 3

**How do nullable data types affect field updates in a PATCH request?**

- ○ They make fields immutable after creation.
- ○ They ensure values are never null.
- ○ They always default fields to zero or empty strings.
- ✅ They allow fields to be set to null explicitly when updating resources.

> **Correct!** Nullable types allow you to safely set values to null during updates.

---

## Question 4

**What HTTP status code is typically returned when a resource is successfully deleted?**

- ○ `200 OK`
- ○ `404 Not Found`
- ○ `201 Created`
- ✅ `204 No Content`

> **Incorrect if answered `200 OK`.** While `200` indicates success, `204 No Content` is more semantically precise for deletion — it signals success with no response body.

---

## Question 5

**What does the HTTP PUT method do when used on an API endpoint?**

- ○ Updates part of the resource
- ○ Appends new data to the existing resource
- ○ Deletes the resource
- ✅ Replaces the entire resource with new data

> **Correct!** PUT replaces the entire existing resource with the provided data.

---

## Question 6

**What is an essential purpose of field validation when creating API resources?**

- ○ To limit the data length for performance
- ○ To prevent data from being processed
- ○ To automatically generate data fields
- ✅ To ensure data quality and format adherence

> **Correct!** Validation maintains data integrity by enforcing correct formats and constraints.

---

## Question 7

**What is a common strategy for handling errors in RESTful APIs?**

- ○ Always return a `500` status code for any error
- ○ Re-try failed requests automatically
- ○ Ignore minor errors to keep responses clean
- ✅ Use specific status codes and include error messages

> **Correct!** Specific codes and messages help users understand and resolve issues.

---

## Question 8

**When should you use the HTTP PATCH method in RESTful APIs?**

- ○ When deleting a resource
- ○ When replacing the entire resource
- ○ When creating a new resource
- ✅ When updating only a part of a resource

> **Correct!** PATCH is used for partial updates of a resource.

---

## Question 9

**Which of the following is the correct hierarchy from most destructive to least destructive in terms of data alteration in RESTful APIs?**

- ○ `POST, GET, PUT, DELETE, PATCH`
- ○ `GET, POST, PATCH, PUT, DELETE`
- ○ `PATCH, DELETE, PUT, GET, POST`
- ✅ `DELETE, PUT, PATCH, POST, GET`

> **Correct!** This order reflects the most-to-least impact on data modification.

---

## Question 10

**Why might you use a PATCH instead of a PUT request when updating a resource?**

- ○ PATCH automatically validates data types.
- ○ PATCH must be used for all updates.
- ○ PATCH is faster because it uses a different protocol.
- ✅ PATCH allows for partial updates instead of full replacements.

> **Correct!** PATCH is beneficial for partial updates where only some fields change.

---