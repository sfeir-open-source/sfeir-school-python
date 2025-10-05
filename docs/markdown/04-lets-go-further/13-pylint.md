<!-- .slide: -->

# Pour aller plus loin - 10

**Qualité de code : Linters & Formatters**

- Permettent d'imposer ces règles !
- **Linters** : Analyse statique du code (détecte erreurs, bugs, style (sans exécuter))
  - `pylint`, `flake8`
  - `ruff` (moderne, rapide)
- **Formatters** : Mise en forme automatique.
  - `autopep8`, `yapf`
  - `black`, `ruff format` (moderne)

##==##

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 10

**Exemple : Avant**

Un code avec des problèmes de style et des erreurs potentielles.

```python
# Fichier: messy_code.py
import os, sys

def my_function(name):
    unused_variable = "hello"
    if name is "John":
        print("Hello John")

my_function ("Jane")
```

##++##

##++## class="with-code"
<br><br><br><br>
**Exemple : Après `ruff` & `black`**
Le même code, automatiquement corrigé et formaté.
```python
# Fichier: clean_code.py
import os
import sys


def my_function(name):
    _unused_variable = "hello"  # Marqué comme inutilisé
    if name == "John":
        print("Hello John")


my_function("Jane")
```

##==##

<!-- .slide: -->

# Pour aller plus loin - 10

**Intégration Continue (CI)**

Automatisez la qualité de code !
* pre-commit hooks : Valide le code avant chaque git commit.
* GitHub Actions / GitLab CI : Valide le code à chaque push.

➡️ Assure un code propre et cohérent dans toute l'équipe.
