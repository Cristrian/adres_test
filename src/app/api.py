from fastapi import FastAPI
from app import schemas
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app import bs_logic as bl

app = FastAPI()

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
def update_acquisition(item: schemas.UpdateAcquisition):
    resp = bl.insert_acquisition(jsonable_encoder(item))
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))


# Create history
@app.post("/history")
def create_history(item: schemas.Record):
    resp = bl.insert_acquisition(jsonable_encoder(item))
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))
# Read history


@app.get("/history")
def read_history(search_criteria: dict):
    resp = bl.insert_acquisition(jsonable_encoder(search_criteria))
    return JSONResponse(content=resp.get("content"),
                        status_code=resp.get("status_code"))
