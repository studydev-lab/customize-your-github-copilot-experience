# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework to practice routing, request/response models, and CRUD-style operations.
Students will create endpoints, validate input data, and return consistent JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI application with basic routes for a task manager API.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py` and run it with Uvicorn.
- Implement `GET /` that returns a welcome JSON message.
- Implement `GET /tasks` that returns the current in-memory task list.


### 🛠️ Add Task Creation and Validation

#### Description
Implement an endpoint to create tasks using request body validation with Pydantic models.

#### Requirements
Completed program should:

- Define a `TaskCreate` model with fields: `title` (required), `completed` (default `False`).
- Implement `POST /tasks` to add a task and auto-assign an integer `id`.
- Return proper HTTP status code (`201`) and the created task as JSON.


### 🛠️ Implement Update and Delete Operations

#### Description
Complete the API by adding update and delete functionality for individual tasks.

#### Requirements
Completed program should:

- Implement `PUT /tasks/{task_id}` to update title/completed status.
- Implement `DELETE /tasks/{task_id}` to remove a task and return a success message.
- Return `404` JSON errors when `task_id` does not exist.
