The purpose of this repository is to store practical challenges and exercises created while learning FastAPI.

## Challenge 01 — Consuming an API

Consume the JSONPlaceholder API using Python.

**Endpoint:** `https://jsonplaceholder.typicode.com/posts`

### Requirements

* `GET` — Get all posts.
* `GET` — Get a post by ID.
* `POST` — Create a new post.
* `PUT` — Update a post.
* `DELETE` — Delete a post.
* Handle the API responses using Python.

## Challenge 02 — Consuming the DummyJSON API

Consume the DummyJSON Products API using FastAPI and HTTPX.

**Endpoint:** `https://dummyjson.com/products`

### Requirements

* `GET` — Get all products.
* `GET` — Get a product by ID.
* `GET` — Search products using a query parameter.
* `POST` — Create a new product.
* Validate parameters using `Annotated`, `Path` and `Query`.
* Handle errors using `try/except`, `HTTPException` and `raise_for_status()`.
* Use `Depends` to practice dependency injection.