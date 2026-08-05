# Task Manager API

A simple RESTful Task Manager API built using **FastAPI** and **Pydantic**. 

## Features
- **Create Task (`POST /tasks`)**: Create a new task with a mandatory title.
- **Get All Tasks (`GET /tasks`)**: Retrieve a list of all existing tasks.
- **Get Task by ID (`GET /tasks/{id}`)**: Fetch details of a specific task.
- **Update Task (`PUT/PATCH /tasks/{id}`)**: Update task title, description, or status.
- **Delete Task (`DELETE /tasks/{id}`)**: Remove a task by its ID.

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic
