from fastapi import FastAPI
from data.database import test_database_connection

app = FastAPI()


@app.on_event("startup")
def startup_event():
    test_database_connection()