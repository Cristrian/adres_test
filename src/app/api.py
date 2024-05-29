from pathlib import Path
from typing import Optional
from fastapi import FastAPI
from src.app import schemas
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.app import bs_logic as bl
from src.setup import setup_database 
app = FastAPI()


if not Path('adres.db').is_file():
    setup_database()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/test")
def create_acquisition(item: schemas.Acquisition):
    itm = jsonable_encoder(item)
    resp = {"content": itm,
            "status_code": 200}
    
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))

# Create adquisitions
@app.post("/acquisition")
def create_acquisition(item: schemas.Acquisition):
    resp = bl.insert_acquisition(jsonable_encoder(item))
    
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))


# Read adquisitions
@app.post("/acquisition:search") 
def read_acquisition(search_criteria: dict):
    resp = bl.search_acquisitions(jsonable_encoder(search_criteria))
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))

# Update adquisitions
# Deactivate adquisitions
@app.put("/acquisition")
def update_acquisition(id:int, item: schemas.UpdateAcquisition):
    resp = bl.update_acquisition(id, jsonable_encoder(item, exclude_none=True))
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))

# Read Record

@app.get("/record")
def read_history(date: str = None):
    resp = bl.search_record(date=date)
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))
