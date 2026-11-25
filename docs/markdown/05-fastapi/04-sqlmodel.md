<!-- .slide: class="with-code" -->

# API Python

**SQLModel : Pydantic et SQLAlchemy dans une seule classe**

- Même auteur que FastAPI : les modèles sont les mêmes que pour la validation.
- `table=True` : la classe devient une table SQL.
- `Field(primary_key=True)` : la clé primaire, attribuée par la base.

```python
from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class MessageBase(SQLModel):
    author: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=500)

class Message(MessageBase, table=True):    # table=True : la table "message"
    id: int | None = Field(default=None, primary_key=True)
    creation_date: datetime = Field(default_factory=lambda: datetime.now(UTC))
```

Notes:
SQLModel combine Pydantic (validation, sérialisation) et SQLAlchemy (requêtes, tables). Même auteur que FastAPI, donc les deux s'enchaînent naturellement.
`id: int | None = None` : tant que l'objet n'est pas enregistré, l'id est vide. La base l'attribue au `commit()`.
`default_factory` appelle la fonction à chaque création d'objet, donc la date est celle de l'enregistrement, en UTC.
SQLModel envoie des requêtes paramétrées : une valeur contenant une apostrophe, ou ressemblant à du SQL, est enregistrée comme du texte, sans risque d'injection. Le test `test_apostrophe_is_stored_as_text` du lab le montre.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Les dépendances : `Depends`**

- Une **dépendance** est une fonction dont une route a besoin (une session de base de données...).
- La route la déclare en paramètre : FastAPI l'appelle et lui passe le résultat.

```python
def get_session():                  # la dépendance : prépare ce dont la route a besoin
    return "ma session"

SessionDep = Annotated[str, Depends(get_session)]

@app.get("/a")
async def route_a(session: SessionDep):   # FastAPI appelle get_session(), puis la route
    return {"session": session}

@app.get("/b")
async def route_b(session: SessionDep):   # même dépendance, réutilisée
    return {"session": session}
```

<!-- .element: class="medium-code" -->

Notes:
Idée à faire passer : on ne crée pas soi-même ce dont la route a besoin, on le déclare, et FastAPI le fournit. On parle d'injection de dépendances.
Ici la dépendance renvoie simplement une chaîne. La slide suivante montre le cas réel : une session de base de données, ouverte avant la route et fermée après, grâce à `yield`.
Avantages : une seule définition, nettoyage automatique, et remplaçable pour les tests (`dependency_overrides`) sans toucher au code des routes.
Les imports (`Annotated`, `Depends`, `FastAPI`) sont ceux des slides précédentes. Une dépendance peut elle-même dépendre d'autres dépendances : pas besoin d'aller plus loin en initiation.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Engine et session : la dépendance de la base**

- L'`engine` connaît la base. SQLite : un simple fichier, sans rien à installer.
- Une `AsyncSession` par requête, fermée à la fin : c'est la dépendance `get_session`.

```python
from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

# En production, seule cette URL change : "postgresql+asyncpg://..."
engine = create_async_engine("sqlite+aiosqlite:///messages.db")

async def get_session() -> AsyncGenerator[AsyncSession]:
    async with AsyncSession(engine) as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
```

<!-- .element: class="medium-code" -->

Notes:
SQLModel n'est pas une base de données : c'est la couche entre Python et le moteur. Ici le moteur est SQLite (`aiosqlite` est son pilote asynchrone). Avec PostgreSQL, on changerait l'URL.
`get_session` est un générateur avec `yield` (comme vu dans le bloc précédent) : ce qui précède `yield` s'exécute avant la route, ce qui suit s'exécute à la fin. La session est donc toujours fermée.
Le fichier `steps/fastapi/messages.db` sera aussi utilisé par le lab MCP : les messages créés dans l'API sont visibles par l'agent.
Le squelette du step-02 fournit déjà tout cela, ainsi que la création de la table au démarrage.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Créer, lire, lister, supprimer**

- `add` puis `commit` pour enregistrer, `refresh` pour récupérer l'id.
- `get` pour un id, `select` pour une liste. Chaque appel à la base s'attend avec `await`.

```python
# Créer : add, commit, puis refresh pour récupérer l'id
message = Message.model_validate(message_in)
session.add(message)
await session.commit()
await session.refresh(message)

# Lire un message : None si absent
message = await session.get(Message, message_id)

# Lister, trié par id
result = await session.exec(select(Message).order_by(Message.id))
messages = result.all()

await session.delete(message)
await session.commit()
```

Notes:
`Message.model_validate(message_in)` convertit le modèle d'entrée (`MessageCreate`) en objet table. Le lab le fait dans `create_message`.
Après `commit`, SQLAlchemy marque les attributs comme périmés. `refresh` recharge l'objet depuis la base : l'id et les valeurs générées sont à jour avant de renvoyer la réponse.
`session.add` est le seul appel sans `await` : il ne fait que ranger l'objet en mémoire, c'est `commit` qui écrit dans la base.
`order_by` est indispensable : sans lui, l'ordre des résultats n'est pas garanti.
Les snippets sont des fragments : `select` vient de `sqlmodel`, `session` et `message_in` viennent de la route.
