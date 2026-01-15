from celery import Celery
import requests
import csv
import os


celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)


@celery.task
def fetch_users_to_csv():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()

    users = response.json()

    os.makedirs("data", exist_ok=True)

    file_path = "data/users.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email"])

        for user in users:
            writer.writerow([user["id"], user["name"], user["email"]])

    return f"{file_path} created"