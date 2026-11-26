# SFEIR School Python

<p align="center">
 <img style="display:block" width="20%" height="20%" src="./docs/assets/images/sfeir-school-logo.png" alt="SFEIR School logo">
</p>

<br/>

[Discover the SFEIR Schools](https://www.sfeir.com/fr/contenus-dexperts/sfeir-school)

## Slides

Vous pouvez consulter les slides [ici](https://sfeir-open-source.github.io/sfeir-school-python/).

Pour les lancer en local :

```bash
cd docs
npx serve
```

Puis ouvrez http://localhost:3000/.

Ou, sans Node.js, avec Docker :

```bash
cd docs
docker compose up
```

Puis ouvrez http://localhost:4242/.

## Prérequis

- **git**
- **uv** (gestionnaire de projets et de versions Python) : [installation](https://docs.astral.sh/uv/getting-started/installation/)
- Un **agent de code IA** pour l'atelier MCP : Claude Code, Codex ou opencode

Inutile d'installer Python vous-même : uv télécharge automatiquement la bonne version (3.14).

## Installation

```bash
git clone https://github.com/sfeir-open-source/sfeir-school-python.git
cd sfeir-school-python
uv sync
uv run python steps/step-00/check_env.py
```

- `uv sync` crée l'environnement virtuel `.venv` et installe toutes les dépendances. À faire une seule fois.
- `uv run ...` exécute une commande dans cet environnement, sans avoir à l'activer.
- `check_env.py` vérifie la version de Python et l'installation des bibliothèques. Il doit afficher `✅ Environnement prêt pour les ateliers.`

## Organisation des exercices

Chaque exercice existe en deux versions :

- `steps/step-XX` : l'énoncé, à compléter ;
- `steps/step-XX-solution` : le corrigé.

Les exercices de FastAPI et de MCP suivent la même logique :

- `steps/fastapi/step-0X` et `steps/fastapi/step-0X-solution` ;
- `steps/mcp/step-01` et `steps/mcp/step-01-solution` (un seul lab), plus `steps/mcp/step-02-bonus`.

Les exercices Python (étapes 01 à 03) et le lab MCP sont des **codes à trous** : remplacez chaque `___` dans `main.py` (`server.py` pour MCP), puis lancez `verifier.py`. Chaque exercice affiche ✅ ou ❌ :

```bash
uv run python steps/step-01/verifier.py            # ❌ tant que les trous ne sont pas complétés
uv run python steps/step-01-solution/verifier.py   # ✅ : c'est le corrigé
uv run python steps/mcp/step-01/verifier.py        # le lab MCP, même principe
```

Chaque exercice Python (étapes 01 à 03) propose aussi **trois exercices bonus** (4 à 6), plus difficiles, pour ceux qui ont terminé : il n'y a pas de trous, seulement une consigne dans la docstring, à vous d'écrire la fonction. Ils sont vérifiés par le même `verifier.py` (`Bonus : 0/3` tant qu'ils ne sont pas faits) et n'empêchent pas le `3/3` des exercices principaux.

Les labs FastAPI contiennent des tests pytest, à lancer depuis la racine du projet :

```bash
uv run pytest -q --tb=short steps/fastapi/step-01   # échoue tant que vous n'avez pas implémenté l'exercice
uv run pytest steps/fastapi/step-01-solution   # passe : c'est le corrigé
```

Les tests de l'énoncé deviennent verts quand votre implémentation est correcte.

## Lancer l'API FastAPI

```bash
uv run fastapi dev steps/fastapi/step-02-solution/main.py
```

Puis ouvrez http://127.0.0.1:8000/docs pour accéder à la documentation interactive de l'API.

## Lancer le serveur MCP

```bash
uv run fastmcp dev inspector steps/mcp/step-01-solution/server.py
```

Cette commande lance l'inspecteur MCP. Le détail de l'atelier est dans les slides.

## Sans uv (optionnel)

Si vous ne pouvez pas installer uv, utilisez un environnement virtuel classique avec Python 3.14.

Linux et macOS :

```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell ou invite de commandes) :

```bat
py -3.14 -m venv .venv
.venv\Scripts\activate
```

Puis installez les dépendances :

```bash
pip install "fastapi[standard]" sqlmodel fastmcp pytest ruff httpx
```

Les commandes se lancent ensuite sans `uv run` : `python steps/step-00/check_env.py`, `pytest steps/fastapi/step-01`, `fastapi dev ...`, `fastmcp dev inspector ...`.

## Aide

- [Documentation Python](https://docs.python.org/3/)
- [Tutoriel FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [Documentation SQLModel](https://sqlmodel.tiangolo.com/)
- [Documentation Pydantic](https://docs.pydantic.dev/latest/)
- [Documentation Model Context Protocol](https://modelcontextprotocol.io/)
- [Documentation FastMCP](https://gofastmcp.com/)

## Pour les mainteneurs

- Utilisez uv et vérifiez que les exercices fonctionnent toujours après une modification.
- Pour générer un `requirements.txt` à l'intention de ceux qui n'ont pas uv :

```bash
uv pip compile pyproject.toml -o requirements.txt
```
