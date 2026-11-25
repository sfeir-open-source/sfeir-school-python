"""BONUS : générer un serveur MCP automatiquement à partir de l'API FastAPI.

`FastMCP.from_fastapi(app)` lit l'application FastAPI (son schéma OpenAPI) et crée
un tool par route : GET /messages, POST /messages, PATCH /messages/{id}, etc.
C'est le prototype le plus rapide, mais il a des limites :

- les noms et descriptions viennent des routes : un tool `read_message_messages`
  dit peu de choses à un LLM, alors qu'un tool `get_message` avec une docstring ciblée
  est bien plus efficace (voir steps/mcp/step-01-solution) ;
- les tools reproduisent la structure HTTP : l'agent doit enchaîner plusieurs appels, et
  les erreurs HTTP (404, 422) sont moins parlantes qu'une ToolError en français ;
- toutes les routes sont exposées, y compris celles qu'un agent ne devrait pas utiliser
  (suppression, par exemple) ;
- la requête passe par l'API en mémoire (httpx + ASGI) : le lifespan de FastAPI n'est pas
  exécuté, d'où la création explicite des tables dans le bloc __main__ ci-dessous.

Conclusion : pour un vrai besoin, concevoir des tools sur mesure. Le from_fastapi est
utile pour explorer rapidement une API existante.

Lancement (le serveur est lancé par l'agent, en stdio) :
    uv run python steps/mcp/step-02-bonus/server.py
"""

import asyncio
import importlib.util
import sys
from pathlib import Path

from fastmcp import FastMCP
from sqlmodel import SQLModel

# L'application FastAPI du lab 2 : steps/fastapi/step-02-solution/main.py
# parents[0] = step-02-bonus, parents[1] = mcp, parents[2] = steps
FASTAPI_MAIN = Path(__file__).resolve().parents[2] / "fastapi" / "step-02-solution" / "main.py"


def load_fastapi_module():
    """Charge le fichier main.py du lab FastAPI comme un module Python."""
    # Le nom de la table SQL est "message" : si le module a déjà été chargé dans ce processus
    # (ex. par les tests), SQLAlchemy refuserait une seconde déclaration. On retire donc
    # la définition précédente de la table ; le schéma est identique.
    if "message" in SQLModel.metadata.tables:
        SQLModel.metadata.remove(SQLModel.metadata.tables["message"])
    spec = importlib.util.spec_from_file_location("messages_api_step02", FASTAPI_MAIN)
    module = importlib.util.module_from_spec(spec)
    sys.modules["messages_api_step02"] = module
    spec.loader.exec_module(module)
    return module


api = load_fastapi_module()

# Un tool par route de l'API FastAPI.
mcp = FastMCP.from_fastapi(app=api.app)


if __name__ == "__main__":
    # Le lifespan de FastAPI n'est pas exécuté par from_fastapi : on crée les tables ici.
    asyncio.run(api.create_tables())
    # Transport stdio par défaut. Ne jamais écrire avec print() : stdout est le canal du protocole.
    mcp.run()
