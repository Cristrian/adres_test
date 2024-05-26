import os
from dotenv import load_dotenv
import uvicorn
load_dotenv(override=True)

if __name__=='__main__':
    # Set up database

    uvicorn.run("app.api:app", 
                host=os.environ.get("HOST"), 
                port=int(os.environ.get("PORT")), 
                reload=True)