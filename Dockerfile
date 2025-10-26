# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /code

# copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application
COPY . .

# expose the FastAPI default port
EXPOSE 8000

# start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
