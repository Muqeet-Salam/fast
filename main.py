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

# Load student data from CSV
df = pd.read_csv("q-fastapi.csv")  # Assuming the file is named students.csv

@app.get("/api")
async def get_students(classes: Optional[List[str]] = Query(None, alias="class")):
    # Convert DataFrame to list of dicts
    students_data = df.to_dict("records")
    
    # Filter by classes if specified
    if classes:
        students_data = [student for student in students_data 
                        if student["class"] in classes]
    
    return {"students": students_data}