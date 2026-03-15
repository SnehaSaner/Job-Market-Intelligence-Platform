import pandas as pd
import re

df = pd.read_csv("jobs_data.csv")

# remove empty rows
df = df.dropna(subset=["job_title"])

# combine all text columns
df["all_text"] = (
    df["job_title"].astype(str) + " " +
    df["company"].astype(str) + " " +
    df["location"].astype(str)
).str.lower()

skills = [
"python",
"sql",
"power bi",
"tableau",
"excel",
"machine learning",
"aws",
"snowflake",
"etl",
"data visualization"
]

skill_count = {}

for skill in skills:
    skill_count[skill] = df["all_text"].str.contains(skill).sum()

skill_df = pd.DataFrame(skill_count.items(), columns=["skill","count"])

print(skill_df)