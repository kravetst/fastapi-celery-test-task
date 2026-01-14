from fastapi import FastAPI, HTTPException
from app.storage import get_tasks, add_task, update_task, delete_task
from app.schemas import Task
from celery_worker import fetch_users_to_csv

app = FastAPI()


@app.get("/tasks")
def read_tasks():
    return get_tasks()


@app.post("/tasks")
def create_task(task: Task):
    return add_task(task.model_dump())


@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: Task):
    updated = update_task(task_id, task.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    deleted = delete_task(task_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted


@app.post("/export-users")
def export_users():
    fetch_users_to_csv.delay()
    return {"status": "task started"}