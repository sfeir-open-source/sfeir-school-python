<!-- .slide: class="with-code" -->

# API Python

**FastAPI**

- **Rapide** : l'un des frameworks Python les plus performants, construit sur Starlette.
- **Typé** : les annotations de type servent à valider, documenter et compléter le code.
- **Auto-documenté** : Swagger UI (`/docs`) générée depuis le code.
- **Validation** : données contrôlées par Pydantic, erreurs renvoyées en JSON.
- **Asynchrone** : `async def` et `await`, comme vu dans le bloc précédent.

![](./assets/images/fastapi.png 'center')

Notes:
FastAPI s'appuie sur deux briques : Starlette pour le routage et le serveur ASGI, Pydantic pour la validation des données.
Les benchmarks le placent parmi les frameworks Python les plus rapides. Ne pas citer de chiffre sans l'avoir mesuré : les résultats dépendent du matériel et de la charge.
Les annotations de type ne sont pas décoratives : FastAPI les lit à l'exécution pour valider les entrées, générer la documentation et typer l'autocomplétion.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Installer, lancer et Swagger**

```bash
uv run fastapi dev main.py
```

- Application servie sur [http://127.0.0.1:8000](http://127.0.0.1:8000), rechargée à chaque sauvegarde.
- Documentation interactive (Swagger) sur [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) : routes, paramètres, réponses, et bouton « Try it out ».

![](./assets/images/swagger.png 'center')

Notes:
`fastapi[standard]` est déjà dans `pyproject.toml` : `uv sync` a tout installé. Pour un nouveau projet, ce serait `uv add "fastapi[standard]"`. La CLI `fastapi` remplace le vieux `uvicorn main:app --reload`.
Le rechargement automatique est pratique pour les labs, à ne pas utiliser en production (`fastapi run`).
Ouvrir /docs dans le navigateur pendant la démo : déplier une route, cliquer sur « Try it out », exécuter.
Le schéma affiché vient des annotations de type et des modèles Pydantic : sans modèle, Swagger ne peut rien montrer de précis.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Paramètres de chemin et de requête**

- Paramètre de chemin : dans l'URL, entre accolades, comme `{message_id}`.
- Paramètre de requête : après le `?`, avec une valeur par défaut.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/messages/{message_id}")          # chemin : {message_id}
async def read_message(message_id: int):    # converti en int, sinon erreur 422
    return {"id": message_id}


@app.get("/messages")                       # ex. /messages?author=Alice&limit=5
async def list_messages(author: str | None = None, limit: int = 20):
    return {"author": author, "limit": limit}
```

Notes:
Le type `int` du paramètre de chemin fait deux choses : conversion (`"3"` devient `3`) et validation (`"abc"` donne une erreur 422).
Tout paramètre de la fonction qui n'est pas dans le chemin devient un paramètre de requête. Avec une valeur par défaut, il est optionnel ; sans valeur par défaut, il est obligatoire.
Des contraintes sont possibles (`Query(ge=1, le=100)`), mais ne sont pas nécessaires pour les labs.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Codes de statut et `HTTPException`**

- `status_code=201` pour une création, `204` pour une suppression sans contenu.
- Pour une erreur, on lève une `HTTPException` : on ne renvoie pas un dictionnaire.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()
messages = {1: "Bonjour"}


@app.get("/messages/{message_id}")
async def read_message(message_id: int):
    if message_id not in messages:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"id": message_id, "message": messages[message_id]}
```

Notes:
Le lab step-01 fait la même chose avec son dictionnaire de messages, et le step-02 avec la base.
Le `detail` est renvoyé au client dans un JSON `{"detail": "..."}`. Les tests du lab vérifient exactement ce texte.
Rappel des codes utiles : 200 lecture, 201 création, 204 suppression sans contenu, 404 introuvable, 422 donnée invalide.

##==##

<!-- .slide: class="with-code" -->

# API Python

**`def` ou `async def` ?**

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/sync")
def route_sync():                # def : FastAPI l'exécute dans un pool de threads
    return {"mode": "def"}


@app.get("/async")
async def route_async():         # async def : exécutée dans la boucle d'événements
    return {"mode": "async def"}
```

- `async def` : pendant qu'une requête **attend** la base de données, le serveur traite les autres requêtes.
- Mais une `async def` qui appelle du code bloquant (`time.sleep`, requête SQL synchrone) bloque toute l'application.

Notes:
Sur notre API, les routes passent presque tout leur temps à attendre la base de données : en `async def`, ce temps d'attente profite aux autres requêtes. Règle simple : si tout le chemin est asynchrone (accès base avec `AsyncSession`, httpx en mode async), écrire `async def`. Si la fonction appelle une bibliothèque synchrone (requests, sqlite3, SQLModel avec `Session`), écrire `def` : FastAPI la lance dans un pool de threads, sans bloquer.
`async def` n'est pas un gain automatique de vitesse : c'est utile pour attendre sans bloquer (réseau, base de données).
Démo possible : une route `async def` avec `time.sleep(5)` bloque les autres requêtes pendant 5 secondes. La même route en `def` ne bloque rien.
Le lien avec le bloc précédent : `async def` produit une coroutine, exécutée par la boucle d'événements, comme avec `await`.
