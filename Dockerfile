FROM python:3.9-slim

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier tous les fichiers de l'application
COPY . .

# Exécuter l'application
CMD ["python", "app.py"]
