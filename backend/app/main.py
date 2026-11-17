
from fastapi import FastAPI

app = FastAPI(
    title="Legal Metrology Framework",
    description="Research framework for regulatory information extraction and package compliance assessment.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Legal Metrology Framework API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "legal-metrology-framework"
    }
