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
```

2. **Run the Server:**
```bash
uvicorn main:app --reload
```

3. **Interactive API Documentation (Swagger UI):**
Open your browser and navigate to:
http://127.0.0.1:8000/docs
