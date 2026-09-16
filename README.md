# To-Do List API

A simple, in-memory To-Do list API built with Python and FastAPI.

## Prerequisites

- Python 3.9+ or Docker installed

## Running Locally (Without Docker)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the API:**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

## Running with Docker

1. **Build the image:**
   ```bash
   docker build -t todo-api .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 todo-api
   ```
   The API will be available at `http://127.0.0.1:8000`.

## API Endpoints & How to Test

Since this API is built with FastAPI, you can use the built-in interactive Swagger UI to test the endpoints!

**Interactive Docs:**
Just navigate to `http://127.0.0.1:8000/docs` in your browser. You can click on any endpoint, click "Try it out", enter the data, and click "Execute".

Alternatively, you can test using `curl`:

1. **Add a task** (`POST /tasks`)
   ```bash
   curl -X POST "http://127.0.0.1:8000/tasks" -H "Content-Type: application/json" -d '{"title": "Buy groceries"}'
   ```

2. **List all tasks** (`GET /tasks`)
   ```bash
   curl -X GET "http://127.0.0.1:8000/tasks"
   ```

3. **Mark a task as done** (`PATCH /tasks/{id}`)
   *(Replace `{id}` with the ID returned when you added the task)*
   ```bash
   curl -X PATCH "http://127.0.0.1:8000/tasks/{id}"
   ```

## GitHub Integration

This repository includes a GitHub Actions workflow (`.github/workflows/docker-build.yml`). Every time you push to the `main` or `master` branch, GitHub will automatically build the Docker image to ensure the codebase is always in a deployable state.

## Reflection

**What was the trickiest part?**
The most subtle part of a quick, purely in-memory API is choosing the right data structure for storage to ensure fast lookups and updates. I chose a dictionary mapping `task_id` to the task object, rather than a list. A dictionary makes retrieving and updating tasks by ID an O(1) operation, avoiding the need to iterate through a list whenever we want to mark a task as done.

**Why these choices?**
I selected **FastAPI** over alternatives like Flask because of its incredible developer experience. By just defining Pydantic models (`BaseModel`), FastAPI gives us automatic data validation and generates interactive Swagger UI documentation out of the box. This makes testing the API locally effortless and eliminates the need to write separate API docs.

**What to improve if I had another day?**
If I had more time, I would implement the following:
1. **Persistent Storage:** Swap out the in-memory dictionary for a real database (like SQLite or PostgreSQL using SQLAlchemy) so data isn't lost when the server restarts.
2. **Unit Tests:** Add `pytest` to write automated tests for the endpoints.
3. **Data Validation/Edge Cases:** Add constraints (e.g., maximum length for a task title, preventing empty titles).
4. **Delete Endpoint:** Allow removing a task entirely (`DELETE /tasks/{id}`).
