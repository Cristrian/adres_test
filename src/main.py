import os
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
from src.app.api import app
from src.setup import setup_database
load_dotenv(override=True)


    # uvicorn.run("app.api:app", 
    #             host=os.environ.get("HOST"), 
    #             port=int(os.environ.get("PORT")), 
    #             reload=False)