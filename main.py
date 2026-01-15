from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn
from models import Top_terrorists
import pandas as pd
from db import save_top_terrorist



app = FastAPI()

def clean_csv(file):
    df = pd.read_csv(file.file)
    new_df = df.sort_values("danger_rate", ascending=False)
    return new_df[["name", "location", "danger_rate"]]


@app.post("/top-threats")
def top_terrorists(upload_file: UploadFile):
    try:
        if not upload_file.file:
            raise HTTPException(tatus_code=400, detail="No file provided")
        elif upload_file.content_type != "text/csv" :
            raise HTTPException(tatus_code=400, detail="Invalid CSV file")
        else:
            top_ter =  clean_csv(upload_file)
            response = save_top_terrorist(top_ter)
            return response.to_json()

    except HTTPException as e:
        if e.status_code == 503:
            raise HTTPException(tatus_code=503, detail="Database unavailable")
        raise HTTPException(tatus_code=422, detail=e)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)
