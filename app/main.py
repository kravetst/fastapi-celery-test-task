from fastapi import FastAPI, HTTPException
import joblib

from app.storage import get_tasks, add_task, update_task, delete_task
from app.schemas import Task, TaskDescription
from app.celery_worker import fetch_users_to_csv

app = FastAPI()


model = joblib.load("data/task_model.joblib")
vectorizer = joblib.load("data/vectorizer.joblib")


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


@app.post("/predict")
def predict_priority(task: TaskDescription):
    text_vec = vectorizer.transform([task.task_description])
    prediction = model.predict(text_vec)[0]
    return {"priority": prediction}
