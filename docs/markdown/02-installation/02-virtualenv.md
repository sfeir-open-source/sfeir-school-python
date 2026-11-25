# Installation de l’environnement

**Pourquoi utiliser un environnement virtuel (venv) ?**

Un venv est un répertoire isolé qui contient une installation spécifique de Python, ainsi que ses propres bibliothèques.

**Problème** : Sans `venv`, les dépendances de vos projets entrent en conflit.

*Exemple : Projet A veut `requests==2.25.0`, Projet B veut `requests==2.28.0`.*

**Solution** : `venv` crée un "bac à sable" pour chaque projet. Chaque projet a ses propres dépendances, ce qui résout les conflits.

Notes:
Sans venv, toutes les installations `pip` vont dans le Python du système. Deux projets qui veulent des versions différentes d'une même bibliothèque finissent par se marcher dessus.

On ne détaille pas la création d'un venv à la main (`python3 -m venv .venv`, activation, `pip install`) : avec uv, vu plus loin, le venv est créé et utilisé automatiquement, sans activation. Le principe reste le même : un dossier `.venv` dans le projet.
