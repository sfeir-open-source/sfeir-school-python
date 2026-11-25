<!-- .slide: -->

# Pour aller plus loin - 10

**Qualité de code : outils**

* **Linter** : analyse statique, sans exécuter le code (erreurs, bugs probables, style)
  * `ruff check` : écrit en Rust par Astral, très rapide, remplace flake8 et isort
  * `pylint` existe toujours : plus strict, plus lent
* **Formatter** : mise en forme automatique
  * `ruff format` : remplace black, avec le même style
* **Type checkers** : vérifient les annotations sans exécuter
  * `mypy`, `pyright`, et `ty` (Astral, encore en bêta)

Notes:
Un linter détecte les erreurs et les mauvaises pratiques sans lancer le programme. Un formatter ne change que la forme, jamais la logique.
Ruff regroupe l'essentiel : pyflakes (F), pycodestyle (E), isort (I), pyupgrade (UP), bugbear (B). Une seule commande, très rapide. `pylint` reste utile pour des analyses plus poussées.
Les type checkers lisent les annotations du bloc typage. mypy et pyright sont les références ; `ty` est la nouvelle proposition d'Astral, rapide, encore en bêta.

##==##

<!-- .slide: class="with-code tc-multiple-columns col-offset" -->

##++##

# Pour aller plus loin - 10

**Avant : 9 problèmes**

```python
import os                        # linter : import inutilisé
from typing import List          # linter : List obsolète

def moyenne(notes: List[int]) -> float:
    print(f"Calcul")             # linter : f-string inutile
    return sum(notes)/len(notes) # formatter : espaces

titre = 'Moyenne'                # formatter : guillemets
config = {"debug":True,"port":8000}  # formatter : dict
age: int = "36"                  # type checker : str, pas int
moyenne("12")                    # type checker : str, pas list
res: str = moyenne([1])          # type checker : float, pas str
```

##++##

##++## class="with-code"

**Après**

```python
# imports inutiles retirés par ruff check --fix

def moyenne(notes: list[int]) -> float:  # ruff check --fix
    print("Calcul")                  # ruff check --fix
    return sum(notes) / len(notes)   # ruff format

titre = "Moyenne"                    # ruff format
config = {"debug": True, "port": 8000}   # ruff format
age: int = 36                        # corrigé à la main
moyenne([12])                        # corrigé à la main
res: float = moyenne([1])            # corrigé à la main
```

##++##

Notes:
Trois outils, trois rôles, trois exemples chacun.
Linter (`ruff check --fix`) : `import os` n'est jamais utilisé (F401) et disparaît ; `from typing import List` est obsolète depuis Python 3.9 (UP035), `List[int]` devient `list[int]` (UP006) ; `f"Calcul"` n'a aucune variable à insérer (F541), le `f` est retiré. Ces corrections sont sûres, `--fix` les applique seul.
Formatter (`ruff format`) : il ne change que la forme, jamais la logique : `sum(notes)/len(notes)` devient `sum(notes) / len(notes)`, les guillemets simples deviennent doubles (`'Moyenne'` devient `"Moyenne"`), et le dictionnaire reçoit ses espaces (`{"debug":True,"port":8000}` devient `{"debug": True, "port": 8000}`). Il gère aussi les lignes vides entre fonctions et les lignes trop longues.
Type checker (`ty`, `mypy`, `pyright`) : il signale mais ne corrige pas. `age: int = "36"` met un texte dans un entier, `moyenne("12")` passe un texte au lieu d'une liste, `res: str = moyenne(...)` stocke un `float` dans un `str`. C'est au développeur de choisir la correction : c'est la différence avec les deux autres outils.
Les exemples ont été vérifiés : `ruff check --fix` puis `ruff format` produisent exactement la colonne de droite, hors les trois lignes de type, et `ty check` signale bien les trois erreurs de la colonne de gauche.

##==##

<!-- .slide: -->

# Pour aller plus loin - 10

**Intégration Continue (CI)**

Automatisez la qualité de code !
* pre-commit hooks : Valide le code avant chaque git commit.
* GitHub Actions / GitLab CI : Valide le code à chaque push.

➡️ Assure un code propre et cohérent dans toute l'équipe.
