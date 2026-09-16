from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI(title="To-Do List API")

class Task(BaseModel):
    title: str

class TaskOut(Task):
    id: str
    completed: bool

# In-memory storage for tasks
tasks_db = {}

@app.post("/tasks", response_model=TaskOut)
def add_task(task: Task):
    """Add a new task to the list."""
    task_id = str(uuid.uuid4())
    new_task = {"id": task_id, "title": task.title, "completed": False}
    tasks_db[task_id] = new_task
    return new_task

@app.get("/tasks", response_model=list[TaskOut])
def list_tasks():
    """List all tasks."""
    return list(tasks_db.values())

@app.patch("/tasks/{task_id}", response_model=TaskOut)
def mark_task_done(task_id: str):
    """Mark a specific task as completed."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db[task_id]["completed"] = True
    return tasks_db[task_id]
