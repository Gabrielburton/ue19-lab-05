# Image de base contenant Python 3
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dependances
COPY requirements.txt .

# Installer les dependances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le programme Python
COPY app.py .

# Lancer l'application
CMD ["python", "app.py"]
