FROM python:3.12

# Update packages and install necessary system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory into the container
COPY . .

# Expose port 8000 to access the API
EXPOSE 8000

# Start the FastAPI application using Uvicorn
CMD ["sh", "-c", "ls -la /app && echo $PYTHONPATH && uvicorn app.main:app --host 0.0.0.0 --port 8000"]