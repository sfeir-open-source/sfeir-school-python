# Brancher votre serveur MCP à un agent

Ce document explique comment enregistrer un serveur MCP **local** (transport `stdio`) dans
**Claude Code**, **Codex** ou **opencode**. Les commandes ci-dessous lancent votre serveur
avec `uv` ; l'agent le démarre lui-même et lui parle via son entrée et sa sortie standard.

## Avant de commencer

1. **Remplacez `/CHEMIN/ABSOLU/VERS/sfeir-school-python`** par le chemin absolu du repo sur votre
   machine, par exemple `/Users/vous/git/sfeir-school-python`. Si le chemin contient des espaces,
   mettez-le entre guillemets.
2. **Pointez vers votre propre dossier**, `steps/mcp/step-01/server.py`, et non vers
   `step-01-solution`. Les commandes ci-dessous utilisent `step-01`.
3. Vérifiez d'abord que le serveur démarre : `uv run python steps/mcp/step-01/server.py`.
   Il ne doit rien afficher et attendre des messages sur l'entrée standard : `Ctrl+C` pour l'arrêter.

## Claude Code

```bash
claude mcp add messages -- uv run --directory /CHEMIN/ABSOLU/VERS/sfeir-school-python python steps/mcp/step-01/server.py
```

- Vérifier : `claude mcp list`, puis dans Claude Code la commande `/mcp`.
- Pour partager la configuration avec l'équipe (fichier `.mcp.json` à la racine du repo), ajoutez
  `--scope project` juste après `add messages`.

## Codex (CLI OpenAI)

```bash
codex mcp add messages -- uv run --directory /CHEMIN/ABSOLU/VERS/sfeir-school-python python steps/mcp/step-01/server.py
```

- Vérifier : `codex mcp list`. La commande écrit dans `~/.codex/config.toml` :

  ```toml
  [mcp_servers.messages]
  command = "uv"
  args = ["run", "--directory", "/CHEMIN/ABSOLU/VERS/sfeir-school-python", "python", "steps/mcp/step-01/server.py"]
  ```

## opencode

Lancez la commande depuis la racine du repo : opencode écrit la configuration du projet
dans `opencode.json` (dossier courant).

```bash
cd /CHEMIN/ABSOLU/VERS/sfeir-school-python
opencode mcp add messages -- uv run --directory /CHEMIN/ABSOLU/VERS/sfeir-school-python python steps/mcp/step-01/server.py
```

Résultat dans `opencode.json` (format d'opencode 2.x, testé avec la version 2.0.32) :

```json
{
  "mcp": {
    "servers": {
      "messages": {
        "type": "local",
        "command": ["uv", "run", "--directory", "/CHEMIN/ABSOLU/VERS/sfeir-school-python", "python", "steps/mcp/step-01/server.py"]
      }
    }
  }
}
```

- Vérifier : `opencode mcp list`.

## Inspecteur MCP (sans agent)

Pour voir les tools, les resources et les prompts, et appeler un tool à la main :

```bash
cd /CHEMIN/ABSOLU/VERS/sfeir-school-python
uv run fastmcp dev inspector steps/mcp/step-01/server.py
```

L'inspecteur utilise `npx` : Node.js doit être installé. Il ouvre une interface dans le navigateur.

## Dépannage

- **Le serveur n'apparaît pas dans l'agent** : relancez l'agent (ou une nouvelle session), puis
  vérifiez avec la commande `list` correspondante (`claude mcp list`, `codex mcp list`,
  `opencode mcp list`).
- **`uv` introuvable depuis l'agent** : l'agent n'utilise pas forcément votre `PATH` de terminal.
  Remplacez `uv` par son chemin complet (`which uv` ; par exemple `/Users/vous/.local/bin/uv`).
- **Chemins relatifs ou incomplets** : `--directory` doit pointer vers le repo en chemin absolu ;
  le chemin `steps/...` est ensuite relatif à ce dossier.
- **Un tool manque** : c'est normal si son décorateur n'est pas encore ajouté.
  `uv run python steps/mcp/step-01/verifier.py` indique précisément ce qui reste à écrire.
- **`no such table`** : le serveur crée les tables au démarrage (`init_db()`). Relancez-le ;
  si l'erreur persiste, vérifiez le chemin de `messages.db` dans `server.py`.
- **Ne jamais écrire avec `print()` dans un serveur `stdio`** : stdout est le canal du protocole,
  un texte parasite casse la connexion. Les messages de débogage doivent aller sur stderr :

  ```python
  import sys

  print("debug", file=sys.stderr)
  ```

  Les logs de FastMCP et les erreurs Python vont sur stderr : ils ne cassent pas la connexion.
