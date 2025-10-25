# FastAPI Task Automation
A production-grade FastAPI microservice designed for backend task automation with JWT authentication, PostgreSQL database, Celery + Redis background jobs, Docker and CI/CD integration, and automated testing.

---

## Day 1 — Project Initialization
Goal: create the base FastAPI project structure, set up a virtual environment, install dependencies, and verify that the API runs locally.

### Achievements
- Initialized Git repository and Python virtual environment  
- Installed FastAPI, Uvicorn, SQLAlchemy, Pydantic, Psycopg2-Binary, and Python-Dotenv  
- Added base route (`GET /`) returning a startup message  
- Verified server runs on http://127.0.0.1:8000  

---
## Day 2 — Database Integration (PostgreSQL + SQLAlchemy + Alembic)

### Goal
Integrate a production-ready relational database layer using Dockerized PostgreSQL, SQLAlchemy ORM, and Alembic migrations.

### Achievements
- 🐘 Deployed PostgreSQL 16 inside Docker (`pg-fastapi` container with volume `pgdata_fastapi`)
- 🔗 Configured `.env` with `DATABASE_URL` for dynamic connection management
- 🧩 Added `app/database.py` to handle SQLAlchemy engine, session factory, and Base class
- 📦 Implemented `app/models.py` with `Task` ORM model
- 🧠 Created Pydantic schemas in `app/schemas.py` for request/response validation
- 🛠️ Added CRUD logic (`app/crud.py`) and modular router (`app/routers/tasks.py`)
- 🚀 Updated `app/main.py` to register routers and initialize the FastAPI app
- ⚙️ Initialized **Alembic** for schema versioning  
  - Configured `alembic.ini` and dynamic `.env` loading in `alembic/env.py`
  - Generated first migration: `create tasks table`
  - Applied migration via `alembic upgrade head`  
- ✅ Verified connectivity with Dockerized PostgreSQL container on port 5433

### Quick Reference Commands
```bash
# Run PostgreSQL in Docker (persistent volume)
docker run --name pg-fastapi \
  -e POSTGRES_USER=task_user \
  -e POSTGRES_PASSWORD=task_pass \
  -e POSTGRES_DB=task_db \
  -p 5433:5432 \
  -v pgdata_fastapi:/var/lib/postgresql/data \
  -d postgres:16

# Apply database migrations
alembic revision --autogenerate -m "create tasks table"
alembic upgrade head

# Start the FastAPI server
uvicorn app.main:app --reload
---
## Quick Start

```bash
# 1. Clone repository
git clone git@github.com:SulimanKh87/fastapi-task-automation.git
cd fastapi-task-automation

# 2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate      # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run FastAPI server
uvicorn app.main:app --reload

Then open http://127.0.0.1:8000
```
Visit:
http://127.0.0.1:8000
 → root message
http://127.0.0.1:8000/docs
 → Swagger UI (auto docs)

## System Architecture

```mermaid
flowchart TD
    A["Client UI (Browser / Postman / CLI)"] --> B["FastAPI Application (app/main.py + Routes)"]
    B --> C["Business Logic Layer (CRUD, Services, Auth)"]
    C --> D["Database Layer (SQLAlchemy + PostgreSQL)"]
    C --> E["Async Worker (Celery + Redis Queue)"]
    E --> F["CI/CD Pipeline (Docker + GitHub Actions)"]
    D --> F

```

**Key Components**
- **FastAPI** — REST API framework (main entry point)
- **SQLAlchemy / PostgreSQL** — relational data storage
- **Celery + Redis** — asynchronous background task queue
- **Docker + GitHub Actions** — containerization & CI/CD automation
- **Pytest** — testing & coverage for backend logic

```markdown
## API Workflow Overview
```mermaid
sequenceDiagram
    participant Client
    participant FastAPI
    participant Logic
    participant DB
    participant Worker

    Client->>FastAPI: Send HTTP Request (JSON)
    FastAPI->>Logic: Validate Input (Pydantic)
    Logic->>DB: Perform CRUD Operation (SQLAlchemy)
    Logic->>Worker: Dispatch Async Job (Celery)
    Worker-->>Logic: Return Job Result
    DB-->>Logic: Confirm Data Stored
    Logic-->>FastAPI: Return Response Object
    FastAPI-->>Client: JSON Response
```        
🧠 Workflow Summary
Client sends an HTTP request (e.g., POST /tasks)
FastAPI receives → validates via Pydantic Schemas
Business Logic executes CRUD via SQLAlchemy models
Celery Worker performs async jobs if needed
Database stores data (PostgreSQL engine)
FastAPI returns a JSON response to the client

```markdown
## Project Structure
```
graph TD
    A[fastapi-task-automation/] --> B[app/]
    B --> C[__init__.py]
    B --> D[main.py]
    B --> E[database.py]
    B --> F[models.py]
    B --> G[schemas.py]
    B --> H[crud.py]
    B --> I[routers/tasks.py]
    A --> J[alembic.ini]
    A --> K[alembic/]
    A --> L[.env]
    A --> M[requirements.txt]

## Dependencies
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-dotenv
pydantic

## License
MIT License
## Author
Suleiman Khasheboun
Email: suli.tempmail2022@gmail.com
GitHub: https://github.com/SulimanKh87