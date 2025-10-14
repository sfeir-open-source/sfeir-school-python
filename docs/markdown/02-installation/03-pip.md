# Installation de l’environnement

**`pip`, le gestionnaire de paquets Python**

- Référence des paquets : [PyPI](https://pypi.org) (Python Package Index)
- Execution de pip :
  - `python3 -m pip <command> <pkg>`
  - *(venv activated)*`pip <command> <pkg>`
- Toujours utiliser dans un **environnement virtuel** !

**Commandes de base**

- Installer un paquet : `pip install <pkg>`
- Lister les paquets installés : `pip list`
- Geler les dépendances : `pip freeze > requirements.txt`
- Installer depuis un fichier : `pip install -r requirements.txt`

Notes:
`pip` est l'outil standard pour installer des bibliothèques tierces (ex: `requests`, `fastapi`, `pandas`).
- **`requirements.txt`** : Fichier standard pour déclarer et partager les dépendances d'un projet, garantissant la reproductibilité.
