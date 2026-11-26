<!-- .slide: class="with-code" -->

# Pour aller plus loin - 04

**Les lambdas**

* Une fonction anonyme, réduite à une seule expression
* Utile comme argument court, par exemple pour `sorted` :

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
]
print(sorted(people, key=lambda p: p["age"]))
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
```

<!-- .element: class="big-code" -->

Notes:
`key=` attend une fonction qui renvoie la valeur de tri. `lambda p: p["age"]` est une fonction sans nom : `p` est le paramètre, `p["age"]` la valeur renvoyée.
Ne pas assigner une lambda à une variable (`f = lambda x: ...`) : c'est contraire à PEP 8, et ruff le signale (règle E731). Dans ce cas, on écrit un `def`, qui donne un nom et une docstring.
Une lambda ne contient qu'une expression : pas d'affectation, pas de boucle. Au-delà, c'est un `def`.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 04

**Les compréhensions de liste**

* Créer une liste à partir d'un itérable, en une seule expression
* Syntaxe : `[expression for élément in itérable if condition]`
* La clause `if` est facultative, plusieurs `for` sont possibles

```python
carres = [x * x for x in range(6)]
print(carres)  # [0, 1, 4, 9, 16, 25]

pairs = [x for x in range(10) if x % 2 == 0]
print(pairs)   # [0, 2, 4, 6, 8]
```

<!-- .element: class="big-code" -->

Notes:
Lire une compréhension comme la boucle : d'abord `for x in range(6)` (on parcourt), puis `x * x` (on produit la valeur).
La clause `if` filtre : seuls les éléments qui la vérifient sont produits.
Les compréhensions sont plus courtes qu'une boucle, mais pas à tout prix : au-delà de deux niveaux, une boucle classique reste plus lisible.

##==##

<!-- .slide: class="with-code tc-multiple-columns col-offset" -->

##++##

# Pour aller plus loin - 04

**Des boucles aux compréhensions**

```python
numbers = [1, 2, 3, 4, 5, 6]

result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n * n)
```

##++##

##++## class="with-code"

Même résultat :

```python
numbers = [1, 2, 3, 4, 5, 6]

result = [n * n for n in numbers if n % 2 == 0]
print(result)  # [4, 16, 36]
```

##++##

Notes:
La transformation est mécanique : la variable de la boucle devient l'expression, la condition du `if` devient la clause `if`, et `append` disparaît.
C'est le principe de l'exercice 2 du lab step-03 : trier avec une lambda, puis filtrer avec une compréhension.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 04

**Compréhensions de set et de dict**

```python
letters = {letter for letter in "aaaaaab"}
print(letters)  # {'a', 'b'} (l'ordre peut varier)

lengths = {word: len(word) for word in ["python", "ruff"]}
print(lengths)  # {'python': 6, 'ruff': 4}
```

<!-- .element: class="big-code" -->

* Avec des parenthèses à la place des crochets : une expression génératrice, paresseuse (cf. générateurs)

Notes:
- Set : `{...}` sans `:`. Les doublons disparaissent. Depuis Python 3, la représentation est `{'a', 'b'}` : l'ancienne écriture `set([...])` n'est plus affichée.
- L'ordre d'un set n'est pas garanti, et il peut changer d'une exécution à l'autre pour les chaînes. Pour un ordre stable, on utilise une liste.
- Dict : `clé: valeur`. Les dict conservent l'ordre d'insertion depuis Python 3.7.
- Piège : `{}` crée un dict vide. Pour un set vide, on écrit `set()`.
