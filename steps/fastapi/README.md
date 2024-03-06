<!-- PROJECT LOGO -->
<br />
<div>
<h2 align="center">SFEIR School Python - FastAPI</h2>
</div>

### Installation des dépendances

L'API va utiliser différents modules Python. S'ils ne sont pas installés sur votre machine, vous pouvez les installer avec la commande suivante `python -m pip install -r requirements.txt`.

### Création de la base de données

L'API va se connecter à une base de données pour écrire ou lire du contenu. Pour initialiser la base et créer les tables nécessaires, lancez la commande `python init_db.py`.

### Démarrage de l'application

Pour démarrer l'API, lancez la commande `uvicorn main:app` dans un terminal. Des logs devraient apparaître. Pour arrêter le service, tapez `Control` + `C`.

### Accès à l'API

Pour accéder à l'API, allez sur http://127.0.0.1:8000/. Vous pouvez consulter http://127.0.0.1:8000/docs ou http://127.0.0.1:8000/redoc pour lire la documentation de l'API.

### Besoin d'aide ?

Voici quelques liens qui pourraient vous aider lors des exercises :
* [Les types en Python](https://fastapi.tiangolo.com/python-types/)
* [Tutoriel FastAPI](https://fastapi.tiangolo.com/tutorial/)
* [Documentation Databses](https://www.encode.io/databases/)
* [Documentation Pydantic](https://pydantic-docs.helpmanual.io/)
