# Installation de l’environnement

**Installer Python 3.14**

* Avec uv (recommandé dans cette formation) : `uv python install 3.14`
* Ou depuis https://www.python.org/downloads/
* Vérifier : `python3 --version` (sous Windows : `python --version`) affiche `Python 3.14.x`

Notes:
Cette formation utilise Python 3.14. Le fichier `pyproject.toml` du dépôt exige `requires-python = ">=3.14"` : un interpréteur plus ancien sera refusé par `uv sync`.

Deux façons d'installer Python. La plus simple : laisser uv installer l'interpréteur, avec `uv python install 3.14`. uv gère lui-même les versions de Python, sur toutes les plateformes ; les slides suivantes présentent uv. L'autre option est l'installateur officiel sur python.org, ou votre gestionnaire de paquets habituel (apt, brew, winget…).

Si vous avez déjà Python 3.14, rien à faire. Vérifiez la version avec la commande ci-dessus. Si `python3` affiche une autre version, utilisez uv : il n'a pas besoin d'un Python déjà installé pour installer une version précise.
