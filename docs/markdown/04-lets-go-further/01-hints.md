<!-- .slide: -->
# Pour aller plus loin - 01

**Typage : les type hints**

* Annotations facultatives, qui décrivent les types attendus
* Aucun effet à l'exécution : Python ne bloque rien
* Utiles pour l'IDE, la lecture du code et les assistants IA
* Vérifiés par mypy, pyright ou ty, **pas à l'exécution**, sauf avec Pydantic (cf. FastAPI)

Notes:
Les annotations sont des métadonnées : Python les stocke, mais ne les contrôle pas. Une fonction annotée `x: int` accepte une chaîne sans broncher à l'exécution.
Ce sont des outils externes (mypy, pyright, ty) qui lisent les annotations et signalent les incohérences avant l'exécution. L'IDE fait la même chose en temps réel.
Exception à retenir : Pydantic lit les annotations et valide les données à l'exécution. C'est la base de FastAPI, on le verra au bloc 5.
Les annotations servent aussi aux assistants IA : plus le contrat d'une fonction est précis, plus les suggestions sont justes.

##==##

<!-- .slide: class="with-code" -->
# Pour aller plus loin - 01

**Typage : un exemple**

* Sans annotation :

```python
def is_palindrome(s):
    return s == s[::-1]
```

<!-- .element: class="big-code" -->

* Avec annotation :

```python
def is_palindrome(s: str) -> bool:
    return s == s[::-1]
```

<!-- .element: class="big-code" -->

Notes:
`s: str` décrit le type du paramètre, `-> bool` celui du retour. Le code est identique : seul le contrat change.
Un type checker signale `is_palindrome(42)` avant l'exécution. Python, lui, ne s'en rend compte qu'au moment où il exécute `42[::-1]`, et lève alors une `TypeError`.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 01

**Typage : génériques, union et alias**

```python
# list[str] : le type des éléments est dans le type (plus de List)
# str | None : « un texte, ou rien » : il faut gérer le None
def first(words: list[str]) -> str | None:
    return words[0] if words else None

scores: dict[str, int] = {"Ada": 36}  # clés str, valeurs int

type UserId = int  # alias : un nom plus parlant, pas un nouveau type

# Rien n'est vérifié à l'exécution : c'est pour l'éditeur
```

<!-- .element: class="big-code" -->

Notes:
- `list[str]` et `dict[str, int]` : génériques natifs depuis Python 3.9. Avant, il fallait `from typing import List, Dict`.
- `str | None` : union écrite avec `|`, syntaxe native depuis Python 3.10. L'ancienne écriture était `Optional[str]`. `None` est une valeur possible : le type checker oblige à la gérer avant d'utiliser la valeur.
- `type UserId = int` : instruction `type` (PEP 695, Python 3.12). Avant 3.12, on écrivait `UserId = int`. Un alias ne crée pas un nouveau type : `UserId` et `int` sont interchangeables. Pour un type distinct, on utilise `typing.NewType`.
- Les versions indiquent quand la syntaxe est apparue, pas une limite : tout fonctionne en 3.13, 3.14 et 3.15.
- Pour valider vraiment des données (requêtes HTTP, fichiers de configuration), c'est Pydantic, vu avec FastAPI.

