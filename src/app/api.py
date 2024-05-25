from fastapi import FastAPI

app = FastAPI()


# Create adquisitions
@app.post("/acquisition")
def create_acquisition():
    return
# Read adquisitions
@app.get("/acquisition")
def read_acquisition():
    return
# Update adquisitions
# Deactivate adquisitions
@app.put("/acquisition")
def update_acquisition():
    return


# Create history
@app.post("/history")
def create_history():
    return
# Read history
@app.get("/history")
def read_history():
    return
