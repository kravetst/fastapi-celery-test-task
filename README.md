# FastAPI + Celery + ML Task Priority Project

This project demonstrates:

- FastAPI for CRUD tasks and REST API
- Celery + Redis for asynchronous tasks
- Machine learning for task priority prediction

## Project structure

```bash
fastapi-celery-test-task/
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
├── train_model.py
├── tests.py
├── data/                 # there will be CSV and ML models, no commits
│   ├── tasks.csv
│   ├── task_model.joblib
│   ├── vectorizer.joblib
│   └── users.csv
└── app/
    ├── main.py           # FastAPI
    ├── celery_worker.py  # Celery tasks
    ├── schemas.py        # Pydantic schemas
    └──storage.py        # "database" for tasks
```
### Installation
Create a virtual environment:
```bash
python -m venv .venv

source .venv/Scripts/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```

### Getting Started

Build and run the project using Docker Compose:
```bash
docker compose up --build
```

Train ML model (creates task_model.joblib and vectorizer.joblib):
```bash
docker compose run --rm web python train_model.py
```

## API Endpoints:

GET /tasks – get all tasks

POST /tasks – create a task

PUT /tasks/{task_id} – update a task

DELETE /tasks/{task_id} – delete a task

POST /export-users – trigger async export to users.csv via Celery

POST /predict – predict task priority

## Example request for prediction:

curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{"task_description": "Update user profile page"}'

Response:

{
  "priority": "low"
}

## Notes

The data/ folder is mounted as a volume, so generated CSV and ML files will persist locally.

Do not commit generated files (tasks.csv, users.csv, task_model.joblib, vectorizer.joblib).

Use requirements.txt for dependencies. Make sure joblib, pandas, scikit-learn, fastapi, celery, and redis are included.