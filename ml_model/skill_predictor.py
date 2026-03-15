import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "jobs_data.csv")

df = df.dropna(subset=["job_title"])

X = df["job_title"]

# NEW TARGET
y = df["job_title"].str.contains("power bi", case=False).astype(int)

print("Class distribution:")
print(y.value_counts())

vectorizer = CountVectorizer()

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()

model.fit(X_vec, y)

print("Model trained successfully")