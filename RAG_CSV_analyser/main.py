from fastapi import FastAPI
from routes import router

app = FastAPI()

# Include API routes
app.include_router(router)

# Root endpoint
@app.get("/")
def home():
    return {"message": "RAG CSV Analyzer API is running!"}
