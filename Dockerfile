FROM python:3.10-slim

# Instala las dependencias necesarias para psycopg
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app/api

# Configura el PYTHONPATH
ENV PYTHONPATH=/app/api

COPY api ./api

RUN pip install --no-cache-dir -r ./api/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
