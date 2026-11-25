<!-- .slide: class="with-code" style="font-size: 0.6em;" -->

# MCP : donner des outils à l'IA

**Brancher votre serveur à un agent**

Remplacez `/CHEMIN/ABSOLU/VERS/sfeir-school-python` par le chemin absolu du repo.

**Claude Code**

```bash
claude mcp add messages -- uv run --directory /CHEMIN/ABSOLU/VERS/sfeir-school-python python steps/mcp/step-01/server.py
```

**Codex**

```bash
codex mcp add messages -- uv run --directory /CHEMIN/ABSOLU/VERS/sfeir-school-python python steps/mcp/step-01/server.py
```

**opencode** (depuis la racine du repo)

```bash
opencode mcp add messages -- uv run --directory /CHEMIN/ABSOLU/VERS/sfeir-school-python python steps/mcp/step-01/server.py
```

- Vérifier : `/mcp` dans Claude Code, `codex mcp list`, `opencode mcp list`.
- Serveur absent ? Relancez l'agent ou ouvrez une nouvelle session.
- Votre serveur est lancé par l'agent (transport **stdio**) : ne jamais écrire avec `print()`, stdout est le canal du protocole. Utilisez stderr.
- Détails et dépannage : `steps/mcp/CONNECT.md`.

Notes:
Les commandes sont celles de `steps/mcp/CONNECT.md`. Elles lancent le serveur avec `uv` : l'agent le démarre lui-même.
Claude Code : `claude mcp list` affiche aussi la liste. `--scope project` écrit la configuration dans `.mcp.json` pour la partager avec l'équipe.
Codex écrit la configuration dans `~/.codex/config.toml`, sous `[mcp_servers.messages]`.
opencode écrit la configuration dans `opencode.json` du dossier courant : d'où le `cd` avant la commande.
Si `uv` est introuvable depuis l'agent, remplacez `uv` par son chemin complet (`which uv`).
