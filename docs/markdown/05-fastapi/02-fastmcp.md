
<!-- .slide: class="with-code" -->

# API Python

**FastMCP**

- Le but d'un serveur MCP est de transformer vos fonctions Python en "outils" qu'un LLM peut appeler.
- FastMCP peut boostrap une API FastAPI pour prototyper un serveur MCP consommant votre API!
- Attention c'est à usage de test. Les LLM obtiennent des performances nettement meilleures avec des serveurs MCP sur-mesure qu'avec des serveurs OpenAPI convertis automatiquement.

##==##

<!-- .slide: -->

# API Python

**Petit aperçu**

```python
from fastmcp import FastMCP
from models import Product
from services import product_service
from api import app

mcp = FastMCP.from_fastapi(app=app)

@mcp.tool
def get_product_information(product_id: int) -> Product | dict:
    """
    Utilise cet outil pour obtenir les informations complètes d'un produit
    quand tu connais son identifiant numérique.
    """
    # L'outil MCP appelle LA MÊME instance partagée du service que l'API.
    product = product_service.get_product_by_id(product_id)
    if not product:
        # On retourne une donnée structurée que le LLM peut comprendre.
        return {"error": f"Le produit avec l'ID {product_id} n'a pas été trouvé."}
    return product

if __name__ == "__main__":
    mcp.run()
```
