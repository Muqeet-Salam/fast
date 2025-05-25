from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List, Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load student data (replace with your CSV path)
df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
async def get_students(classes: List[str] = Query(None, alias="class")):
    students_data = df.to_dict("records")
    if classes:
        students_data = [s for s in students_data if s["class"] in classes]
    return {"students": students_data}