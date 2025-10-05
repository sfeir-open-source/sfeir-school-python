<!-- .slide: -->

# Pour aller plus loin - 10

**Les bonnes pratiques - convention de nommage**

* Python utilise des PEP (Python Enhancement Proposal) :
  * Proposer des évolutions au langage
  * Partager les bonnes pratiques
* PEP 8 - Style Guide for Python Code :
  * https://www.python.org/dev/peps/pep-0008/
* PEP 20 - The Zen of Python :
  * https://www.python.org/dev/peps/pep-0020/


##==##

<!-- .slide: -->

# Pour aller plus loin - 10

**Les bonnes pratiques - disposition du code**

*   **Indentation**: 4 espaces.
*   **Longueur de ligne**: 79 caractères (souvent 120).
*   **Sauts de ligne**:
    *   2 lignes pour séparer fonctions et classes.
    *   1 ligne pour séparer les méthodes dans une classe.
*   **Encodage**: UTF-8 par défaut en Python 3.

**Exemple de formatage de ligne longue :**
```python
# Bonne pratique: alignement vertical ou indentation suspendue
def ma_super_fonction_avec_un_nom_tres_long(
        param1, param2, param3,
        param4, param5, param6):
    print("Hello")

# Opérateurs en début de ligne pour la lisibilité
total = (valeur_un
         + valeur_deux
         - valeur_trois)
```

##==##

<!-- .slide: -->

# Pour aller plus loin - 10

**Les bonnes pratiques - imports 👍**
```python
# 1. Librairies standards (alphabétique)
import json
import os

# 2. Librairies tierces (alphabétique)
import requests
from fastapi import FastAPI

# 3. Modules locaux (alphabétique)
from my_app import models
from my_app.utils import helper
```
**À éviter 👎**
```python
# Imports groupés et désordonnés
import requests, os # NON
from math import * # NON

# Imports relatifs peu clairs
from .. import utils # NON
```

##==##

<!-- .slide: -->

# Pour aller plus loin - 10

**Les bonnes pratiques - Espacement & Style**

 Recommandation | Good 👍                | Bad 👎                          |
|---|------------------------|---------------------------------|
| Pas d'espaces autour des parenthèses | `print('hello')`       | `print ('hello')`               |
| Espace après une virgule | `ma_liste = [1, 2, 3]` | `ma_liste = [1,2,3]`            |
| Un seul espace pour l'assignation | `x_=_1`                | `x__=__1`                       |
| Cohérence des guillemets | `name = "Sfeir"`       | `name = 'Sfeir' # Inconsistant` |
| Pas d'espace en fin de ligne | `ma_ligne()`           | `ma_ligne() `                   |


##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 10

**Les bonnes pratiques - documentation**

* Un bloc de commentaire doit se faire avec des # :

```python
# First line
# Second line
```

<!-- .element: class="big-code" -->

* Tout module, fonction ou classe doit avoir une docstring :

```python
def function():
  """My function"""
  pass
```

<!-- .element: class="big-code" -->

Notes:
Docstring : permet de documenter la fonctionnalité macro de la fonction (paramètre, retour).

Commentaire (bloc ou ligne) : utile pour les détails d’implémentation.


##==##

<!-- .slide: -->

# Pour aller plus loin - 10

**Les bonnes pratiques - conventions de nommage**

| Type | Convention | Exemple |
|---|---|---|
| Variable, Fonction, Module | `snake_case` | `ma_variable`, `calculer_total()` |
| Classe, Exception | `PascalCase` | `MaClasse`, `ValeurInvalideError` |
| Constante | `UPPER_CASE` | `MA_CONSTANTE`, `TIMEOUT = 30` |
| Méthode d'instance | `self` en 1er | `def get_name(self):` |
| Méthode de classe | `cls` en 1er | `def from_config(cls, config):` |



##==##

<!-- .slide: -->

# Pour aller plus loin - 10

**Les bonnes pratiques - programmation**

| Pratique | Good 👍 | Bad 👎 |
|---|---|---|
| Comparer à `None` | `if my_var is None:` | `if my_var == None:` |
| Exceptions spécifiques | `except ValueError:` | `except Exception:` |
| Retours consistants | `return value` ou `return None` | Retours de types mixtes |
