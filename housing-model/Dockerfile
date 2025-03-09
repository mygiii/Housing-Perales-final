FROM python:3.12

# Update packages and install necessary system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory into the container
COPY /app/ .

# Expose port 8000 to access the API
EXPOSE 8001

# Start the FastAPI application using Uvicorn
CMD ["uvicorn app.train.py:app --host 0.0.0.0 --port 8001"]