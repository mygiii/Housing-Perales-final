FROM python:3.12

WORKDIR /app

# Met à jour la liste des paquets et installe les dépendances système nécessaires
RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copie les scripts consumer.py et producer.py
COPY app/consumer.py /app/consumer.py
COPY app/producer.py /app/producer.py

# Lance le consumer directement
CMD ["python", "consumer.py"]