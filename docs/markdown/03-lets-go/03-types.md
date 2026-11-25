<!-- .slide: -->

# Les bases - 02

**Les types**

| Type | Exemple | Type | Exemple |
|---|---|---|---|
| **bool** | `True` / `False` | **tuple** | `(10, 12)` |
| **int** | `42` (précision non bornée) | **list** | `[15, 15, 16]` |
| **float** | `0.5` | **set** | `{15, 16}` |
| **complex** | `-1j` | **dict** | `{'a': 10, 'b': 11}` |
| **str** | `'hello'`, `'字'` | **bytes** | `b'hello'` |
| **NoneType** | `None` | | |

Notes:
Il n'existe plus de type `long` en Python 3 : `int` gère les entiers de taille quelconque, sans limite fixe. La syntaxe `15L` est une erreur en Python 3.

`None` représente l'absence de valeur. C'est l'unique instance de son type, `NoneType`. On le teste avec `is None`, et non `== None`.

`bytes` est une séquence d'octets immuable (`b'hello'`). Elle sert aux données binaires : fichiers ouverts en mode binaire, réseau.

Tuple ≠ list : le tuple est immuable, la liste est modifiable.

Bonnes pratiques : le tuple sert à une structure hétérogène, où chaque position a un sens (`(10, 12)` = page 10, ligne 12). La liste sert à une séquence homogène dont l'ordre compte (`[12, 13, 14]` = une liste de pages).

##==##

<!-- .slide: -->

# Les bases - 02

**Les conversions de type**

| Expression | Résultat |
|---|---|
| `bool(0)` / `bool(42)` | `False` / `True` |
| `float(42)` | `42.0` |
| `set('hello')` | `{'h', 'e', 'l', 'o'}` (ordre arbitraire) |
| `tuple([1, 2])` | `(1, 2)` |

Notes:
La conversion se fait en appelant le nom du type cible comme une fonction : `int("42")`, `str(3.14)`, `list(range(3))`.

Attention : l'ordre affiché par `set('hello')` n'est pas garanti. Un set n'a pas d'ordre, et l'ordre peut changer d'une exécution à l'autre, car le hachage des chaînes est randomisé. Ne comptez jamais sur l'ordre d'un set.

En Python 3, un set s'affiche `{...}`. La forme `set([...])` appartient à Python 2 et aux anciens tutoriels.
