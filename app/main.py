from fastapi import FastAPI

app = FastAPI(
    title="Cloud Cost Optimization Dashboard",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "project": "Cloud Cost Optimization Dashboard",
        "status": "Running Successfully"
    }