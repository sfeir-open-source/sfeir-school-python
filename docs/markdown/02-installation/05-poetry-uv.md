# Installation de l’environnement

**POETRY / UV**

* **Poetry(legacy)** < **uv(ultra-rapide)**
* Outils tout-en-un : dépendances, packaging, environnements virtuels.
* Fichier `pyproject.toml` pour centraliser la configuration.
```toml
dependencies = [
    "loguru>=0.7.3",
    "typer>=0.15.1",]
```
* Fichier `poetry.lock / uv.lock` pour figer les versions des libs.
