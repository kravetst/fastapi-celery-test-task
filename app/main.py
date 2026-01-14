from fastapi import FastAPI, HTTPException
from app.storage import get_tasks, add_task, update_task, delete_task
from app.schemas import Task

app = FastAPI()


@app.get("/tasks")
def read_tasks():
    return get_tasks()


@app.post("/tasks")
def create_task(task: Task):
    return add_task(task.dict())


@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: Task):
    updated = update_task(task_id, task.dict())
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    deleted = delete_task(task_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
