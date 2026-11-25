# UE19 Lab 05 - app.py

## Description

app.py est une application en Python 3 qui utilise
la librairie Requests pour interroger une API publique.

L'application récupère une blague aléatoire et affiche
sa catégorie, son texte et son identifiant.

## API utilisée

- Nom : Official Joke API
- URL : https://official-joke-api.appspot.com/random_joke
- Méthode HTTP : GET
- Authentification : aucune

## Fonctionnalités

- Récupération d'une blague aléatoire
- Affichage de la catégorie de la blague
- Affichage de la question et de la réponse
- Affichage de l'identifiant de la blague
- Menu interactif
- Possibilité de récupérer plusieurs blagues
- Gestion des erreurs de connexion
- Possibilité de quitter l'application

## Technologies

- Python 3
- Requests
- JSON
- Docker

## Installation

Cloner le repository :

```bash
git clone https://github.com/GabrielBurton/ue19-lab-05.git
cd ue19-lab-05
```

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

## Lancer l'application

Exécuter la commande :

```bash
python app.py
```

Le menu permet de récupérer une blague ou de quitter
l'application.

## Lancer avec Docker

Construire l'image Docker :

```bash
docker build -t random-joke-app .
```

Lancer le conteneur :

```bash
docker run -it --rm random-joke-app
```

## Structure du projet

```text
ue19-lab-05/
├── app.py
├── README.md
├── requirements.txt
└── Dockerfile
```

## Auteur

Votre nom
UE19 - Lab 05
