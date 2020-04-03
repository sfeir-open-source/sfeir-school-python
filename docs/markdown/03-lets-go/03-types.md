<!-- .slide: -->

# Les bases - 02

**Les types**

|         |         |         |         |
| ------- | ------- | ------- | ------- |
| **bool** | True/False | **str** | ‘hello’  // ‘字’ |
| **int** | 42 | **tuple** | (10,12) |
| **long** | 15L | **list** | [15,15,16] |
| **float** | 0.5 | **set** | {15,16} |
| **complex** | -1j | **dict** | {‘a’: 10, ‘b’: 11} |

Notes:
Type “None”

Tuple ≠ list => immutable

Bonne pratiques : tuples : structure de données hétérogènes entre les éléments (chaque entrée peut avoir un sens différent)

list : séquence homogène d’élément dont l’ordre est important

Exemple : (10, 12) => page 10, ligne 12

[12, 13, 14] => liste de pages

##==##
<!-- .slide: -->

# Les bases - 02

**Les conversions de type**

|         |         |
| ------- | ------- |
| bool(0) / bool(42) | False / True |
| float(42) | 42.0 |
| set(‘hello’) | set([‘h’, ‘e’, ‘l’, ‘o’]) |
| tuple([1, 2]) | (1, 2) |

Notes:
La conversion de type est extrêmement simple en Python, servez-vous seulement du nom du type cible comme fonction.
