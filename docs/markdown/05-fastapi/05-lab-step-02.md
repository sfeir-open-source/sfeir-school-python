<!-- .slide: class="exercice" style="font-size: 0.65em;" -->

# API Python

## Exercice (25 minutes)

**step-02 : les messages dans une base SQLite**

- Compléter les TODO de `steps/fastapi/step-02/main.py` (moteur, session et table fournis) :
  - la table : ajouter `creation_date` à `Message`
  - `POST /messages` → 201 : `add`, `commit`, `refresh`
  - `GET /messages/{message_id}` → 404 si absent
  - `GET /messages` → la liste triée par id
- Plus rapides : `PATCH` et `DELETE` (204) sur `/messages/{message_id}`
- Lancer : `uv run fastapi dev steps/fastapi/step-02/main.py`
- Vérifier : `uv run pytest -q --tb=short steps/fastapi/step-02`
- Corrigé : `step-02-solution`

Notes:
Le fichier `steps/fastapi/messages.db` est créé au démarrage de l'application (`lifespan`) : pas besoin de le créer à la main. Il est ignoré par git.
Mêmes routes qu'au step-01, mais le dictionnaire est remplacé par la base : seul le stockage change. Chaque appel à la base s'attend avec `await`.
Insister sur la différence entre `MessageCreate` (ce que le client envoie) et `MessagePublic` (ce que l'API renvoie) : c'est ce que les tests vérifient.
Demander d'envoyer un message contenant une apostrophe (`l'API`) depuis Swagger : il est enregistré sans erreur, car les valeurs sont passées en paramètres.
Le PATCH utilise `exclude_unset=True` : seuls les champs réellement envoyés par le client sont modifiés, c'est la définition d'un PATCH. Les tests de PATCH et DELETE échouent tant que ce bonus n'est pas fait, c'est normal.
