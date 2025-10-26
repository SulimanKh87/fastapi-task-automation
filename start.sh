#!/bin/sh
echo "🟢 Waiting for database..."
sleep 5

echo "🧩 Running Alembic migrations..."
alembic upgrade head

echo "🚀 Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
