import os
import pandas as pd
from pymongo import MongoClient
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("MONGO_HOST")
port = os.getenv("MONGO_PORT")
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
db_name = os.getenv("MONGO_DB")
auth_source = os.getenv("MONGO_AUTH_SOURCE")
url = f"mongodb://{username}:{password}@{host}:{port}"

def get_connection():
    client = MongoClient(url)
    db = client[f'{db_name}']
    return db['top_threats']

def save_top_terrorist(data: pd.DataFrame):
    try:
        conn = get_connection()
        for ter in data:
            conn['top_threats'].insert_one({"aa":"asas"})
        return True
    except HTTPException as e:
        raise e
