FROM python:3.9-slim

# Crear un directori per l'aplicació
WORKDIR /app

# Instal·lar les dependències
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el codi font
COPY . .

# Exposar el port per la API
EXPOSE 8000

# Comanda per executar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
