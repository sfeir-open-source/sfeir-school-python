<!-- PROJECT LOGO -->
<br />
<div>
<h2 align="center">SFEIR School Python - FastAPI</h2>
</div>

### Installation des dépendances

#### Méthode classique

```bash
python --version ## just verify you currently use the python version recommanded by your teacher
python -m venv .venv
source .venv/bin/activate #if you use Linux/MacOS.
.\venv\Scripts\activate #if you use Windows using classic MSDOS Console.
.\venv\bin\activate #if you use Windows using pycharm terminal or powershell console.
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Méthode moderne

```bash
uv venv -p python3.12.11 ## if you want to be 100% sure uv will use the targeted python version
uv sync
uv run uvicorn main:app --reload
```

### Création de la base de données

- L'API va se connecter à une base de données pour écrire ou lire du contenu. 
- Pour initialiser la base et créer les tables nécessaires, lancez la commande `python init_db.py`.

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
