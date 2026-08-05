from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import uuid

app = FastAPI(
    title="Task Manager API",
    description="A CRUD Task Manager API built for assignment submission.",
    version="1.0.0"
)

# In-memory storage for tasks
tasks_db = {}

# Pydantic Model for Task Schema
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Task title (Mandatory, non-empty)")
    description: Optional[str] = Field(None, description="Task details (Optional)")
    status: str = Field("pending", description="Task state (e.g., pending or completed)")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, description="Updated task title")
    description: Optional[str] = Field(None, description="Updated task details")
    status: Optional[str] = Field(None, description="Updated task status")

class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    status: str
    created_at: str

# 1. POST /tasks - Create a new task
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty."
        )
    
    task_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat() + "Z"
    
    new_task = {
        "id": task_id,
        "title": task.title.strip(),
        "description": task.description,
        "status": task.status,
        "created_at": now
    }
    
    tasks_db[task_id] = new_task
    return new_task

# 2. GET /tasks - Retrieve all tasks
@app.get("/tasks", response_model=List[TaskResponse], status_code=status.HTTP_200_OK)
def get_all_tasks():
    return list(tasks_db.values())

# 3. GET /tasks/{id} - Retrieve a specific task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID '{task_id}' not found."
        )
    return tasks_db[task_id]

# 4. PUT / PATCH /tasks/{id} - Update an existing task
@app.put("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
@app.patch("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: str, task_update: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID '{task_id}' not found."
        )
    
    existing_task = tasks_db[task_id]
    
    if task_update.title is not None:
        if not task_update.title.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title cannot be empty."
            )
        existing_task["title"] = task_update.title.strip()
        
    if task_update.description is not None:
        existing_task["description"] = task_update.description
        
    if task_update.status is not None:
        existing_task["status"] = task_update.status
        
    tasks_db[task_id] = existing_task
    return existing_task

# 5. DELETE /tasks/{id} - Remove a task
@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID '{task_id}' not found."
        )
    
    deleted_task = tasks_db.pop(task_id)
    return {"message": "Task successfully deleted", "deleted_task_id": task_id}
