from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks

# Create tables for the first time (temporary before Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Automation API", version="0.2.0")

# Register the /tasks router
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "FastAPI connected to PostgreSQL!"}

@app.get("/health")
def health():
    return {"status": "ok"}
