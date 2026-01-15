import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Loading data
df = pd.read_csv("data/tasks.csv")

X = df["task_description"]
y = df["priority"]

# Text vectorization
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Training a model
model = LogisticRegression()
model.fit(X_vec, y)

# Saving the model and vectorizer
joblib.dump(model, "data/task_model.joblib")
joblib.dump(vectorizer, "data/vectorizer.joblib")

print("Model trained and saved")
