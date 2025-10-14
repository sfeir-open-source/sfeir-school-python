# Installation de l’environnement

**Pourquoi utiliser un environnement virtuel (venv) ?**

Un venv est un répertoire isolé qui contient une installation spécifique de Python, ainsi que ses propres bibliothèques.

**Problème** : Sans `venv`, les dépendances de vos projets entrent en conflit.

*Exemple : Projet A veut `requests==2.25.0`, Projet B veut `requests==2.28.0`.*

**Solution** : `venv` crée un "bac à sable" pour chaque projet. Chaque projet a ses propres dépendances, ce qui résout les conflits.

##==##

<!-- .slide: class="with-code" -->


# Installation de l’environnement

1.  **Créer un environnement virtuel**

    Le module `venv` est inclus dans Python, il n'y a donc rien à installer.
    Créez l'environnement (par convention, on le nomme `.venv`) :
    ```bash
    cd mon-projet/
    python3 -m venv .venv
    ```

2.  **Activer l'environnement**
    ```bash
    source .venv/bin/activate
    ```
    Une fois activé, votre terminal affichera `(.venv)` au début de la ligne.

3.  **Désactiver l'environnement**

    Quand vous avez fini de travailler sur le projet :
    ```bash
    deactivate
    ```

<!-- .element: class="big-code" -->
