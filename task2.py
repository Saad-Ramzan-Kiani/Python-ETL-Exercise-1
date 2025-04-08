# file: exercise2.py
import requests
import pandas as pd
import sqlite3
import os

API_URL = "https://jsonplaceholder.typicode.com/users"

def extract_data():
    response = requests.get(API_URL)
    return response.json()

def transform_data(data):
    return list(map(lambda user: {
        "id": user["id"],
        "name": user["name"].upper(),
        "email": user["email"]
    }, data))

def load_data_to_db(data, db_name="output/users.db"):
    os.makedirs("output", exist_ok=True)
    conn = sqlite3.connect(db_name)
    df = pd.DataFrame(data)
    df.to_sql("users", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data_to_db(transformed_data)
