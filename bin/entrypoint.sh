#!/bin/sh

# Wait for a short period to ensure the database is ready
sleep 5

# Run Alembic migrations
alembic upgrade head

# Start the FastAPI application
uvicorn main:app --host 0.0.0.0 --port 8000