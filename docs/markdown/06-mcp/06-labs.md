<!-- .slide: class="exercice" style="font-size: 0.65em;" -->

# MCP : donner des outils à l'IA

## Exercice (25 minutes)

**mcp step-01 : un serveur MCP sur nos messages**

- Ouvrir `steps/mcp/step-01/server.py` (la base est fournie) : remplacer les `___` et ajouter les décorateurs demandés.
  - Ex. 1 : `count_words` et `now` (avec leur docstring)
  - Ex. 2 : `get_message` (`ToolError`), `post_message`, `search_messages`
  - Ex. 3 : la resource `messages://latest` et le prompt `summarize_messages`
- Vérifier : `uv run python steps/mcp/step-01/verifier.py`
- Brancher dans votre agent (`CONNECT.md`) : « résume les derniers messages »
- Corrigé : `step-01-solution`

Notes:
Les vérifications sont dans `verifier.py`, séparé pour ne pas encombrer `server.py`. Elles utilisent le client en mémoire de FastMCP et une base temporaire : `steps/fastapi/messages.db` n'est jamais touché. En cas de ❌, la ligne de l'`assert` qui échoue s'affiche.
Pour inspecter le serveur sans agent : `uv run fastmcp dev inspector steps/mcp/step-01/server.py` (nécessite Node.js, `npx`). C'est le premier réflexe quand un tool se comporte mal : l'inspecteur affiche ce que l'agent recevrait.
Les décorateurs (`@mcp.tool`, `@mcp.resource`, `@mcp.prompt`) sont demandés en commentaire : c'est volontaire, pour que l'étudiant écrive lui-même la ligne.
L'accès à la base est fourni (`_find_message`, `_save_message`, `_latest_messages`) : c'est le sujet du lab FastAPI, pas celui du lab MCP. Le seul morceau de requête à écrire est le `where(...contains(...))` de `search_messages`.
Le serveur est lancé par l'agent en stdio : ne jamais écrire avec `print()`.

##==##

<!-- .slide: class="exercice" style="font-size: 0.7em;" -->

# MCP : donner des outils à l'IA

## Bonus (10 minutes)

**mcp step-02-bonus : `from_fastapi`**

- Lancer l'inspecteur : `uv run fastmcp dev inspector steps/mcp/step-02-bonus/server.py`
- Lister les tools générés et les comparer avec ceux du step-01 : noms, descriptions, nombre d'appels pour « lire les 3 derniers messages ».
- Discuter des limites : quel tool ne donneriez-vous jamais à un agent ?

Notes:
Le serveur est généré à partir de l'API FastAPI du lab 2 (`steps/fastapi/step-02-solution`). Rien à écrire : on observe et on compare avec le serveur écrit à la main.
Question pour la salle : `delete_message_messages` est exposé sans condition. Un agent peut supprimer des messages sans rien demander.
