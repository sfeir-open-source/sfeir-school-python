<!-- .slide: class="with-code" -->

# MCP : donner des outils à l'IA

**Et si on générait le serveur depuis FastAPI ?**

```python
from fastmcp import FastMCP
from main import app  # l'application FastAPI du lab step-02

mcp = FastMCP.from_fastapi(app=app)

if __name__ == "__main__":
    mcp.run()
```

- `from_fastapi` lit le schéma OpenAPI de l'API et crée **un tool par route**.
- Le prototype le plus rapide pour explorer une API existante.

Notes:
C'est exactement ce que fait le bonus : il charge `steps/fastapi/step-02-solution/main.py`, puis appelle `from_fastapi`.
Pour un prototype, c'est très pratique : quelques lignes et votre API est utilisable par un agent.
Attention : l'API en mémoire est appelée via ASGI. Le lifespan de FastAPI n'est pas exécuté, d'où la création des tables dans le bloc `__main__` du bonus.

##==##

<!-- .slide: class="with-code" style="font-size: 0.85em;" -->

# MCP : donner des outils à l'IA

**Ce que l'agent voit (bonus)**

```text
root
list_messages_messages_get
create_message_messages_post
read_message_messages
delete_message_messages
update_message_messages
```

- Des noms issus des routes : `create_message_messages_post` dit peu de chose à un LLM.
- `delete_message_messages` est exposé : toutes les routes passent, y compris la suppression.

Notes:
Ces noms viennent de l'exécution réelle du bonus (FastMCP 4.2.0). Ils changent si une route change de nom.
La route `root` ne sert à rien pour répondre à une demande de l'utilisateur, mais l'agent la voit et doit l'écarter.
Comparez avec le lab MCP (step-01) : `list_messages`, `post_message`, `search_messages`… des noms qui racontent ce que l'outil fait.

##==##

<!-- .slide: -->

# MCP : donner des outils à l'IA

**Les limites de `from_fastapi`**

- **Vocabulaire HTTP** : l'agent doit enchaîner plusieurs appels, sans vocabulaire métier.
- **Erreurs HTTP** (404, 422) moins parlantes qu'un `ToolError` en français.
- **Tout est exposé** : le modèle peut supprimer des messages sans rien demander.
- **Prototype** : utile pour explorer, pas pour un vrai besoin.

> Les LLM sont bien meilleurs avec des outils pensés pour eux.

Notes:
Un prototype généré montre rapidement ce qui est possible. Pour un usage réel, on écrit des tools sur mesure : quelques outils, des noms clairs, des erreurs utiles, et seulement les actions voulues.
Le lab MCP (step-01) le montre : même base, même API, mais un vocabulaire métier et un choix explicite des outils exposés.
Question pour la salle : quel outil généré par le bonus ne voudriez-vous jamais donner à un agent ?
