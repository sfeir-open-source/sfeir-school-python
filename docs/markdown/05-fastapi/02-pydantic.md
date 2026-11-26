<!-- .slide: class="with-code" -->

# API Python

**Pydantic : validation par les annotations**

- `BaseModel` : une classe dont les annotations sont vérifiées à chaque création.
- Les valeurs sont converties si c'est possible (`"42"` devient `42`), sinon une `ValidationError` est levée.
- `Field` ajoute des contraintes : longueur, bornes, valeur par défaut.

```python
from pydantic import BaseModel, Field, ValidationError


class MessageCreate(BaseModel):
    author: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=500)

print(MessageCreate(author="Alice", message="Bonjour"))
try:
    MessageCreate(author="", message="Bonjour")
except ValidationError as error:
    print(error.errors()[0]["type"])   # string_too_short
```

Notes:
Pydantic applique les annotations à l'exécution. C'est la différence avec ty ou mypy, qui vérifient seulement avant l'exécution.
La conversion est volontaire : `"42"` devient `42` pour un champ `int`. Pour refuser toute conversion, on passe par `Field(strict=True)`.
`error.errors()` renvoie la liste des erreurs. Chaque erreur a un `type` stable (`string_too_short`), utilisable par le client.
Le même `MessageCreate` sert dans le lab : c'est lui qui valide le corps de `POST /messages`.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Erreur de validation : format Pydantic v2**

FastAPI renvoie un statut `422` avec la liste des erreurs :

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "author"],
      "msg": "String should have at least 1 character",
      "input": "",
      "ctx": {"min_length": 1}
    }
  ]
}
```

<!-- .element: class="big-code" -->

Notes:
Ce JSON vient de `POST /messages` avec `{"author": "", "message": "Bonjour"}` dans le lab : l'erreur réelle, pas une version simplifiée.
`type` : identifiant stable de l'erreur. Le test `test_empty_author_returns_422` du lab vérifie `type` et `loc`.
`loc` : l'emplacement de la donnée fautive. Ici `body` puis `author`. Pour un paramètre de chemin ou de requête, ce serait `path` ou `query`.
`msg` : message lisible en anglais, mais `type` et `loc` suffisent pour une application.
Attention : les anciennes documentations montrent le format Pydantic v1 (`type_error.str`). Il n'est plus utilisé.

##==##

<!-- .slide: class="with-code" -->

# API Python

**Modèles d'entrée et de sortie**

- Un modèle par usage : ce que le client envoie, ce que l'API renvoie.
- Le client ne choisit jamais l'`id` ni la date de création.
- Le type de retour (`-> MessagePublic`) filtre et documente la réponse.

```python
class MessageCreate(BaseModel):            # ce que le client envoie
    author: str = Field(min_length=1, max_length=50)
    message: str = Field(min_length=1, max_length=500)


class MessagePublic(MessageCreate):        # ce que l'API renvoie
    id: int
    creation_date: datetime


@app.post("/messages", status_code=201)
async def create_message(message_in: MessageCreate) -> MessagePublic:
    ...
```

Notes:
`MessageCreate` ne contient ni `id` ni date : si le client pouvait les envoyer, il pourrait fixer une date de création arbitraire.
FastAPI utilise le type de retour comme `response_model` : seuls les champs de `MessagePublic` sortent, et Swagger les affiche. Si la fonction renvoie un objet plus riche (comme la table du step-02), il est filtré : c'est aussi une protection contre une fuite de champs sensibles (un mot de passe, par exemple).
Au step-02, on écrit `response_model=MessagePublic` explicitement, car la fonction renvoie un objet `Message` (la table) et non un `MessagePublic`.
Question à poser : pourquoi `MessagePublic` contient-il `id` et `creation_date` alors que `MessageCreate` non ?
