Book Management API (FastAPI & Pydantic)
Hi there! This project is a lightweight REST API built with Python and FastAPI to manage a book inventory.

Coming from a Business Analysis background, I didn't just want to write endpoints that worked—I wanted to make sure the data entering the system actually made sense. This project focuses heavily on strict API data contracts, schema validation, and thinking about the request life-cycle from a product perspective.

Features & Business Logic
Data Integrity First (Strict Validation): Garbage in, garbage out. I used Pydantic models to enforce real business rules right at the API gateway. For example, book descriptions are capped at 100 characters to prevent database bloat, and ratings must legitimately fall between 1.0 and 5.0.

Flexible Querying: I built endpoints that reflect how a user or frontend might actually search for data—whether that's fetching multiple specific books via query lists or filtering inventory by publication date.

Interactive Documentation: Good software needs good docs. I configured custom Pydantic schema examples so the auto-generated Swagger UI is immediately readable, clear, and ready for anyone to test.

Tech Stack
Python

FastAPI

Pydantic v2

API Endpoints Preview
GET /books/ - Fetch the entire book inventory

GET /books/get_book/{book_id} - Fetch a single book by its ID

POST /books/new_books/ - Add a new book (with auto-generating sequential IDs)

PUT /books/update_book - Update an existing book's metrics

DELETE /book/delete_book/{book_id} - Remove a record from the inventory
