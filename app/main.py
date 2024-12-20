from fastapi import FastAPI, File, UploadFile
from app.utils import run_notebooks
import os

app = FastAPI()

@app.post("/process/")
async def process_citizen_card(file: UploadFile):
    file_path = f"data/input/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    result = run_notebooks(file_path)
    return {"result": result}
