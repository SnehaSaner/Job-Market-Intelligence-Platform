import pandas as pd

df = pd.read_csv("jobs_data.csv")

df["title"] = df["job_title"].str.lower()

roles = {
    "data analyst": "data analyst",
    "business analyst": "business analyst",
    "bi analyst": "business intelligence",
    "power bi": "power bi",
    "sql": "sql",
    "data scientist": "data science",
    "machine learning": "machine learning"
}

role_counts = {}

for role, keyword in roles.items():
    role_counts[role] = df["title"].str.contains(keyword, na=False).sum()

result = pd.DataFrame(list(role_counts.items()), columns=["role","count"])

print(result)