<!-- .slide: class="with-code" -->

# MCP : donner des outils à l'IA

**FastMCP**

- Librairie Python pour écrire un serveur MCP : vous écrivez des **fonctions**, FastMCP gère le protocole.
- Déjà installée avec le projet (`fastmcp`, version 4.x).
- Même esprit que FastAPI : décorateurs, type hints, docstrings.

**Vous connaissez déjà les décorateurs !**

Notes:
FastMCP s'occupe de la négociation, du format JSON-RPC, des schémas et du transport. Vous écrivez la logique métier.
Rappel du bloc 4 : `@mcp.tool` enregistre une fonction comme outil, comme `@app.get("/")` enregistre une route dans FastAPI.
Ce n'est pas une API web : les décorateurs ici déclarent des capacités auprès du protocole.

##==##

<!-- .slide: class="with-code" -->

# MCP : donner des outils à l'IA

**Un serveur minimal**

```python
from fastmcp import FastMCP

mcp = FastMCP("messages")


@mcp.tool
def count_words(text: str) -> int:
    """Count the words in a text. Use it when the user asks how many words a text contains."""
    return len(text.split())


if __name__ == "__main__":
    # Transport stdio par défaut
    mcp.run()
```

Notes:
C'est le serveur du lab MCP (solution), réduit à un seul tool. Tout le serveur tient dans ce fichier.
`FastMCP("messages")` donne un nom au serveur : il apparaît dans l'inspecteur et dans l'agent.
`mcp.run()` lance le serveur en stdio : l'agent le démarre et lui parle via stdin / stdout.

##==##

<!-- .slide: class="with-code" style="font-size: 0.85em;" -->

# MCP : donner des outils à l'IA

**La docstring et les type hints forment le contrat**

- Le LLM ne voit pas votre code : il voit le **nom**, la **description** (docstring) et le **schéma** des arguments.
- Les type hints deviennent un JSON Schema. Une valeur par défaut rend l'argument optionnel.
- La docstring dit **quand** appeler l'outil : c'est votre seul levier pour guider le choix.

```json
{
  "name": "count_words",
  "description": "Count the words in a text. Use it when the user asks how many words a text contains.",
  "inputSchema": {
    "type": "object",
    "properties": { "text": { "type": "string" } },
    "required": ["text"],
    "additionalProperties": false
  },
  "outputSchema": {
    "type": "object",
    "properties": { "result": { "type": "integer" } },
    "required": ["result"]
  }
}
```

Notes:
Ce JSON est généré par FastMCP à partir de votre fonction. Vous pouvez le voir dans l'inspecteur, dans l'onglet des tools.
Un argument `timezone: str = "Europe/Paris"` donne un champ `"default"` dans le schéma et n'est pas dans `required`.
La description est le seul texte que le modèle lit pour décider. Une docstring vague donne un outil qui n'est jamais appelé, ou appelé au mauvais moment.

##==##

<!-- .slide: class="with-code" style="font-size: 0.85em;" -->

# MCP : donner des outils à l'IA

**Resource : des données à lire**

```python
@mcp.resource("messages://latest", mime_type="application/json")
def latest_messages_resource() -> str:
    """The 5 most recent messages, as JSON. Read it to get a quick overview of the guestbook."""
    return json.dumps(_latest_messages(5), ensure_ascii=False)
```

- Identifiée par une **URI** (`messages://latest`).
- C'est l'application qui la lit et la met dans le contexte, pas le modèle qui la demande.
- Idéale pour un aperçu : pas besoin d'un appel d'outil.

Notes:
Ce code vient du lab MCP (solution). `_latest_messages` est une fonction auxiliaire qui interroge la base.
Une resource est en lecture seule. Son URI est un identifiant stable : l'agent peut la retrouver avec `resources/list`.
Différence avec un tool : un tool fait quelque chose (calcul, écriture), une resource fournit des données.

##==##

<!-- .slide: class="with-code" style="font-size: 0.85em;" -->

# MCP : donner des outils à l'IA

**Prompt : une commande réutilisable**

```python
@mcp.prompt
def summarize_messages(limit: int = 20) -> str:
    """Ask the assistant to summarise the latest messages of the guestbook."""
    return (
        f"Use the list_messages tool to fetch the {limit} most recent messages. "
        "Then write a short summary in French: the main topics, who wrote what, "
        "and anything that seems to need an answer."
    )
```

- Modèle de message choisi par l'**utilisateur**, souvent proposé comme commande (slash).
- Ses arguments sont les paramètres de la fonction.

Notes:
Ce code vient du lab MCP (solution). Le prompt ne fait rien par lui-même : il renvoie un texte d'instruction que l'utilisateur envoie au modèle.
Il demande au modèle d'appeler un tool, `list_messages`. Un prompt bien écrit guide l'enchaînement des outils.

##==##
<!-- .slide: style="font-size: 0.75em;" -->

# MCP : donner des outils à l'IA

**Concevoir de bons tools**

- **Peu de tools, orientés tâche** : `list_messages`, `post_message`, pas un tool par route ni par colonne.
- **Nom en verbe + objet**, en anglais, et **docstring = mode d'emploi** : ce que fait l'outil, quand l'utiliser.
- **Types précis, défauts raisonnables** : `limit: int = 10` évite de poser une question à l'utilisateur.
- **Sortie concise et structurée** : les données utiles, pas des pages entières de JSON.
- **Erreurs actionnables** : `raise ToolError("Aucun message avec l'identifiant 42.")` part tel quel à l'agent, qui corrige son appel.

| Plutôt | Mieux | Pourquoi |
|---|---|---|
| `db_query(sql)` | `search_messages(query, limit)` | Pas de SQL exposé au modèle |
| `route_42()` | `get_message(message_id)` | Un nom qui dit ce qu'il fait |
| `do_stuff(data: dict)` | `post_message(author, message)` | Des arguments typés et nommés |

Notes:
Un agent choisit ses outils à partir de leurs noms et de leurs descriptions. Chaque outil supplémentaire est un choix de plus pour le modèle, et un risque de mauvais choix. Pensez comme un développeur qui découvre votre API : que doit-il lire pour savoir quoi faire ?
`ToolError` : le message est une consigne pour le modèle, il doit dire ce qui ne va pas et, si possible, comment corriger. Dans le lab MCP, `get_message` lève une `ToolError` quand l'identifiant n'existe pas. Toute autre exception est journalisée par FastMCP, et l'agent reçoit seulement « Error calling tool » avec le message brut.
Le tableau : un outil qui accepte du SQL brut donne au modèle le pouvoir de tout lire, tout modifier, et ouvre la porte aux injections. Un nom généré à partir d'une route ne l'aide pas à choisir. Un `dict` sans structure l'oblige à deviner les clés.
Pour tester sans agent, les tests des labs utilisent `Client(mcp)` (client en mémoire), et l'inspecteur (`fastmcp dev inspector`) affiche ce que l'agent recevrait : les commandes sont sur les slides de lab.
