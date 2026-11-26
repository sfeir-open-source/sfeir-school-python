<!-- .slide: class="with-code" -->

# Le fil rouge

Une API de messages, construite pas à pas pendant la journée :

```text
Python
  │
  ▼
API de messages      FastAPI + SQLModel
  │
  ▼
Serveur MCP          FastMCP
  │
  ▼
Agent IA             Claude Code, Codex, opencode
```

Notes:
Le fil rouge de la formation. Vous commencez par les bases de Python, puis vous utilisez ces notions pour écrire une API de messages avec FastAPI : routes, modèles Pydantic, base de données avec SQLModel.

Dans le dernier bloc, vous exposez cette même API à un agent IA sous forme d'outils MCP. Le serveur MCP est écrit avec FastMCP, et l'agent (Claude Code, Codex ou opencode) appelle ces outils comme il le ferait avec n'importe quel outil local.

Le résultat : un agent capable de lire et d'écrire des messages dans votre API. Cette capture de l'ancienne application « todo » n'est plus affichée, mais le fichier image reste disponible dans le dépôt.
