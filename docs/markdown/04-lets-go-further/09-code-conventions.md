<!-- .slide: -->

# Pour aller plus loin - 09

**Les bonnes pratiques : les PEP**

* Python utilise des PEP (Python Enhancement Proposal) :
  * Proposer des évolutions au langage
  * Partager les bonnes pratiques
* Indentation de 4 espaces, 2 lignes entre fonctions et classes, 1 ligne entre méthodes
* Longueur de ligne : 79 caractères selon PEP 8 (mais dans la pratique souvent plus.)

| Recommandation | Bien 👍 | Mal 👎 |
|---|---|---|
| Pas d'espace avant la parenthèse | `print("hello")` | `print ("hello")` |
| Un espace après une virgule | `ma_liste = [1, 2, 3]` | `ma_liste = [1,2,3]` |
| Un espace de chaque côté de `=` | `x = 1` | `x=1` |
| Un seul style de guillemets par fichier | `name = "Sfeir"` | `'Sfeir'` ici et `"Sfeir"` là |

Notes:
Inutile de tout retenir : `ruff format` applique ces règles automatiquement (slide qualité). Il faut surtout savoir les lire.
Les espaces : PEP 8 demande un espace de chaque côté de `=` pour une affectation, mais pas dans les arguments d'une fonction (`f(x=1)`). Les espaces en fin de ligne sont aussi proscrits : ruff les supprime.
La longueur de 79 caractères est celle de PEP 8. Ce repo utilise 100 caractères, configurés dans `pyproject.toml`. Suivez la règle de votre équipe.

##==##

<!-- .slide: -->

# Pour aller plus loin - 09

**Les bonnes pratiques : nommage**

| Type | Convention | Exemple |
|---|---|---|
| Variable, fonction, module | `snake_case` | `ma_variable`, `calculer_total()` |
| Classe, exception | `PascalCase` | `MaClasse`, `ValeurInvalideError` |
| Constante | `MAJUSCULES` | `TIMEOUT = 30` |
| Méthode d'instance | `self` en premier | `def get_name(self):` |
| Méthode de classe | `cls` en premier | `def from_config(cls, config):` |

Notes:
Un nom décrit un rôle, pas un type : `prix_ttc` vaut mieux que `float1`, et `liste_clients` que `data`.
Un seul underscore en début de nom (`_interne`) signale un usage interne, par convention. Ce n'est pas une protection : Python ne l'impose pas.
`from_config(cls, config)` est un exemple de `classmethod`, vu dans la section classes.

##==##

<!-- .slide: -->

# Pour aller plus loin - 09

**Les bonnes pratiques : programmation et imports**

* Docstring sur chaque module, fonction et classe. Commentaires `#` pour les détails d'implémentation.

| Pratique | Bien 👍 | Mal 👎 |
|---|---|---|
| Tester `None` avec `is` | `if valeur is None:` | `if valeur == None:` |
| Exceptions spécifiques | `except ValueError:` | `except Exception:` |
| Valeur par défaut non mutable | `def f(items=None):` | `def f(items=[]):` |
| Retours cohérents | `return value` ou `return None` | types différents selon le cas |
| Imports : stdlib, tierces, locales | un import par ligne, dans cet ordre | `import os, sys` ; `from math import *` |

Notes:
`is None` compare l'identité avec l'objet `None`, qui est unique. `== None` passe par la méthode `__eq__`, qui peut être surchargée et donner un résultat faux.
Une exception générique (`except Exception`) masque les vraies erreurs (une faute de frappe devient silencieuse). Attrapez l'exception attendue.
La valeur par défaut `[]` est créée une fois : tous les appels partagent la même liste. Mettre `None` puis créer la liste dans la fonction.
Imports : bibliothèque standard, bibliothèques tierces, modules locaux, un import par ligne. `import *` rend l'origine des noms invisible. `ruff` (règle I) vérifie l'ordre.
