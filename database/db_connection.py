import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sneha",
        database="job_market"
    )
    
    return conn