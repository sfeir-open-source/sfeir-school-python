<!-- .slide: class="with-code" -->

# API Python

**FastAPI**

- Framework Web Python 3.6+ pour la création d’API (synchrone ou non).
- Rapide à coder
- Annotations de type
- Documentation automatique (swagger)

![](./assets/images/fastapi.png 'center')

Notes:
Très rapide : La performance est supérieure à Django et Flask et est même comparable aux performances de NodeJS et GO
Annotation de Type (Type hints) : Facilite la validation, permet l'autocomplétion et facilite le debugging
Documentation automatique : FastAPI génère la documentation en format Swagger UI et ReDoc automatiquement.


##==##


<!-- .slide: class="exercice" -->

# API Python

## TP

**step-01 : Premiers pas avec FastAPI**

- Installer les dépendances.
- Démarrer l'application.
- Vérifier que l'API répond `Hello world!`


##==##


<!-- .slide: class="exercice" -->

# API Python

## TP

**step-02 : Ajoutons une base de données**

- Installer la base de données.
- Démarrer l'application.
- Regarder ce que l'API retourne sur les routes `/health` et `/tables`.


##==##


<!-- .slide: class="with-code" -->

# API Python

**Pydantic**

- Validation des données et gestion des paramètres à l'aide des annotations de type.
- Applique les annotations à l'exécution et génère des erreurs si les données ne sont pas valides.
- Retourne les erreurs de validation sous forme de JSON dans une FastAPI

```python
from pydantic import BaseModel
class Car(BaseModel):
    color: str
    gears: int

not_good = Car(color=['b', 'l', 'u', 'e'], gears=4)
```
```json
{
  "detail": [
    {
      "loc": [ "body", "color" ],
      "msg": "str type expected",
      "type": "type_error.str"
    }
  ]
}
```

##==##


<!-- .slide: class="exercice" -->
<!-- .slide: style="font-size: 0.8em;" -->
# API Python

## TP

**step-03 : Créons les modèles**

- Créer trois modèles :
  - `MessageGet` pour les routes `GET`
    - Un message a un `id`, un `author`, une `creation_date`... et le `message` lui-même
  - `MessagePost` pour les routes `POST`
    - Pour créer un message, on a juste besoin de `author` et du `message`
  - `MessageUpdate` pour les routes `PUT`
    - Pour modifier un message, on a juste besoin du `message`


##==##


<!-- .slide: class="exercice" -->

# API Python

## TP

**step-04 : Créons les premières routes**

- Créer deux routes dans l'API :
  - `POST /message` permettant de stocker un message dans la base de données. Cette route devra retourner au moins l'identifiant du message
  - `GET /message/id` retournant le message qui possède comme identifiant `id`


##==##


<!-- .slide: class="exercice" -->
<!-- .slide: style="font-size: 0.8em;" -->
# API Python

## TP

**step-05 : Créons d'autres routes**

- Plus de routes !

  - `GET /messages` pour avoir la liste de tous les messages
  - `PUT /message/id` pour modifier un message
  - `DELETE /message/id` pour supprimer un message

- Pour les plus rapides, il y a encore plus de routes dans `step-bonus-fastapi`.
