<!-- .slide: class="exercice" style="font-size: 0.65em;" -->

# API Python

## Exercice (20 minutes)

**step-01 : une API de messages, sans base de données**

- Compléter les TODO de `steps/fastapi/step-01/main.py` :
  - les modèles `MessageCreate` et `MessagePublic`
  - `POST /messages` → 201
  - `GET /messages/{message_id}` → 404 si absent
  - `GET /messages` → la liste
- Lancer : `uv run fastapi dev steps/fastapi/step-01/main.py`
- Vérifier : `uv run pytest -q --tb=short steps/fastapi/step-01`
- Corrigé : `step-01-solution`

Notes:
Les messages sont gardés dans un dictionnaire en mémoire. Objectif : une API qui répond, validée par Pydantic, testée dans Swagger. Pas de base de données : tout est perdu au redémarrage, c'est voulu, la base arrive au step-02.
Demander d'envoyer un `author` vide depuis Swagger : l'erreur 422 de la slide précédente apparaît pour de vrai.
Les routes sont en `async def`, sans `await` à ce stade : rien n'est asynchrone dans un dictionnaire, mais le step-02 en aura besoin.
Les tests de ce lab n'ont pas besoin de serveur : ils appellent l'application directement. En cas d'échec, `--tb=short` affiche la ligne de l'`assert` qui échoue.
