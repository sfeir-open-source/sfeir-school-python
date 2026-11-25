<!-- .slide: class="with-code" -->

# MCP : donner des outils à l'IA

**MCP, c'est l'USB-C de l'IA**

- **Sans standard** : chaque application IA (Claude Code, Codex, opencode… ou un script maison) a son propre format d'extension. Brancher votre outil sur 3 applications, c'est **3 intégrations différentes**.
- **Avec MCP** : les applications savent déjà parler MCP (leur éditeur l'a fait, ou le SDK MCP pour un script maison). Vous écrivez **un seul serveur**, et il fonctionne partout.
- Protocole ouvert, lancé par Anthropic en novembre 2024.
- Adopté depuis par Claude, ChatGPT et Codex, Gemini, VS Code (Copilot), Cursor, opencode…

Notes:
Comme l'USB-C pour les appareils : un seul type de prise au lieu d'un câble par couple appareil / chargeur.
Le problème est un produit cartésien : N applications × M outils = N × M intégrations (3 × 3 = 9). Avec MCP, on passe à N + M (3 + 3 = 6) : chaque éditeur d'application implémente MCP une fois, chaque auteur d'outil écrit un serveur une fois. C'est l'argument à l'échelle de l'écosystème.
Pour vous, développeur, c'est plus simple : le côté application est déjà fait par l'éditeur (zéro code pour vous). Il reste à écrire votre serveur, une seule fois : votre API de messages sera utilisable dans Claude Code, Codex, opencode, dans vos propres scripts, et dans chaque application qui sortira demain.
Le protocole fixe le format des messages échangés ; le contenu de vos outils reste à écrire : c'est le travail du lab.
MCP est un protocole ouvert, pas un produit : vous pouvez écrire un serveur MCP sans dépendre d'un éditeur.

##==##

<!-- .slide: class="with-code" -->

# MCP : donner des outils à l'IA

**Architecture : host, client, serveur**

```text
HOST = l'application que vous ouvrez (Claude Code, Codex, opencode…)
 ├── Client 1 ──JSON-RPC──▶ Serveur « messages »    <- votre server.py (les labs)
 ├── Client 2 ──JSON-RPC──▶ Serveur « fichiers »
 └── Client 3 ──JSON-RPC──▶ Serveur distant (HTTP)
```

- **Host** : le mot de la **norme** MCP pour l'application que vous utilisez. Elle parle au LLM, affiche tout et demande votre accord.
- Dans le langage courant, on dit plutôt **harness** (harnais) : tout harness est un host, mais un simple chat avec des outils est un host sans être un harness.
- **Client** : une pièce interne du host, **un par serveur** branché. Il parle **JSON-RPC** au serveur (slides suivantes). Les harness le fournisse (donc, pas à écrire) ; si vous construisez votre propre host, vous utilisez généralement le client du SDK MCP.
- **Serveur** : l'exposition des primitives (ressources, tools, prompts). 

Notes:
Le host est l'application que vous utilisez : Claude Code, Codex ou opencode. C'est elle qui contrôle la sécurité : elle demande votre accord avant certains appels.
Vocabulaire : « host » est le terme de la spécification MCP, et il est large : toute application qui intègre un LLM et héberge des clients MCP (un chat, un IDE, un script, un agent). « Harness » (harnais) est le terme courant dans le milieu des agents : le programme construit autour du modèle, avec sa boucle autonome (planification, édition de fichiers, commandes, permissions). Claude Code, Codex CLI et opencode sont des harness. Un harness qui utilise MCP est donc un host ; l'inverse n'est pas vrai. « Harness » ne figure pas dans la spec : vous le lirez dans les articles et sur les réseaux, « host » dans la documentation MCP.
Le client est une pièce technique interne au host. Le host en ouvre un par serveur auquel il est connecté, et chaque client gère sa propre connexion. FastMCP fournit aussi un client (`Client`) : c'est celui que le vérificateur du lab utilise, en mémoire, pour appeler votre serveur. Client et serveur échangent des messages JSON-RPC 2.0 : c'est l'objet des deux slides suivantes.
Exemple : Claude Code (host) crée un client, qui se connecte à votre `server.py` (serveur).
Le serveur est ce que vous écrivez dans les labs : votre `server.py`. Il peut tourner sur votre machine (lancé par le host) ou sur le réseau.
Au démarrage, avant tout échange, le client et le serveur négocient : le client envoie `initialize` (version du protocole, ses capacités), le serveur répond avec les siennes (tools, resources, prompts), puis le client envoie `notifications/initialized`. FastMCP fait tout cela pour vous. À la fin, le client ferme le transport (stdin fermé, connexion coupée).

##==##
<!-- .slide: class="with-code" style="font-size: 0.85em;" -->

# MCP : donner des outils à l'IA

**Les messages : JSON-RPC 2.0**

Le client demande l'appel du tool `count_words`, le serveur répond :

```json
{
  "jsonrpc": "2.0", "id": 2, "method": "tools/call",
  "params": { "name": "count_words", "arguments": { "text": "Bonjour SFEIR School" } }
}
```

```json
{
  "jsonrpc": "2.0", "id": 2,
  "result": { "content": [{ "type": "text", "text": "3" }], "structuredContent": { "result": 3 }, "isError": false }
}
```

- Une **requête** a un `id`, une `method` et des `params`. La réponse reprend le **même `id`**.
- `content` : le texte que reçoit le LLM. `structuredContent` : la donnée typée.
- Erreur d'un tool : `isError: true`, avec le message dans `content`.

Notes:
JSON-RPC 2.0 est un format très simple : du JSON, avec une méthode et des paramètres. Une notification, elle, n'a pas d'`id` et n'attend pas de réponse. Le `id` est ce qui relie la réponse à la question, même si plusieurs appels sont en cours.
Vous n'écrirez jamais ce JSON à la main : FastMCP s'en charge. Mais quand un tool ne répond pas comme prévu, c'est ce message que vous lirez dans l'inspecteur.
La vraie réponse de FastMCP contient aussi un champ `_meta` : il est retiré ici pour la lisibilité.
La distinction importante : une erreur de tool (`isError`) reste une réponse normale du protocole. Une erreur JSON-RPC (champ `error`) signifie que la requête elle-même n'a pas pu être traitée.

##==##

<!-- .slide: class="with-code" style="font-size: 0.8em;" -->

# MCP : donner des outils à l'IA

**Les trois primitives d'un serveur**

| Primitive | Qui décide de l'utiliser ? | Exemple du lab | Méthodes |
|---|---|---|---|
| **Tools** | Le **modèle** appelle l'outil quand il en a besoin | `count_words`, `post_message` | `tools/list`, `tools/call` |
| **Resources** | L'**application** attache des données à lire (URI) | `messages://latest` | `resources/list`, `resources/read` |
| **Prompts** | L'**utilisateur** choisit un modèle de message | `summarize_messages` | `prompts/list`, `prompts/get` |

Notes:
**Tools** : des actions et des calculs. C'est le modèle qui décide de les appeler. L'agent demande en général une validation humaine avant un appel qui modifie quelque chose.
**Resources** : des données en lecture seule, identifiées par une URI (par exemple `messages://latest`). C'est l'application qui choisit ce qu'elle met dans le contexte du modèle.
**Prompts** : des modèles de message réutilisables, souvent proposés comme commandes (slash). C'est l'utilisateur qui les déclenche.
Retenez la question à poser : « qui décide ? ». Elle explique presque tous les choix de conception.
