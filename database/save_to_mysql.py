import mysql.connector
import pandas as pd

df = pd.read_csv("jobs_data.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sneha",
    database="job_market"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    query = """
    INSERT INTO jobs (job_title, company, location)
    VALUES (%s,%s,%s)
    """
    
    cursor.execute(query,(row['job_title'],row['company'],row['location']))

conn.commit()

print("Data inserted into MySQL")

cursor.close()
conn.close()