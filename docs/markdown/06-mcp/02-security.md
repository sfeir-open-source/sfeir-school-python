<!-- .slide: -->

# MCP : donner des outils à l'IA

**Sécurité : un serveur MCP exécute du code pour l'IA**

- **Les descriptions sont lues par le LLM** : un serveur malveillant peut y glisser des instructions. N'installez que des serveurs de confiance.
- **Les résultats des tools sont des données, pas des ordres** : un message ou une page web peut contenir une injection de prompt.
- **Moindre privilège** : n'exposez que ce qui est nécessaire (un tool d'écriture est un risque, une base en lecture seule si possible).
- **Validez les entrées** : type hints, Pydantic, `ToolError`. Jamais de SQL construit avec des f-strings.

Notes:
Un outil MCP peut faire ce que votre compte peut faire. Dès qu'un agent a un outil d'écriture, un texte qu'il lit peut le pousser à l'utiliser.
Exemple du lab : `post_message` écrit dans la base. Un agent qui lit un message piégé pourrait en poster un autre à votre place. D'où l'importance d'une docstring qui limite quand l'outil doit être utilisé, et de la validation humaine : gardez-la active et acceptez les appels de tools qui écrivent un par un.
Côté utilisateur de serveurs : un serveur MCP est un programme qui s'exécute sur votre machine, avec vos droits. Traitez-le comme tel : vérifiez son code avant de l'installer, et utilisez un token limité plutôt que votre accès complet.
