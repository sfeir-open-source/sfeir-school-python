<!-- .slide: class="with-code" -->

# Les bases - 04

**Les idiomes Python : f-strings**

* Une f-string est une chaîne précédée de `f`, avec des expressions entre accolades.
* `=` affiche l'expression et sa valeur, `:` applique un format.

```python
prenom = "Ada"
prix = 12.5

print(f"Bonjour {prenom} !")    # Bonjour Ada !
print(f"{prenom=}")             # prenom='Ada'
print(f"{prix:.2f} €")          # 12.50 €
print(f"[{prix * 2:>10.2f}]")   # [     25.00]
```

<!-- .element: class="big-code" -->

Notes:
Les f-strings (Python 3.6+) remplacent la concaténation avec `+` et l'ancienne méthode `str.format`. L'expression entre accolades est évaluée à l'exécution : n'importe quelle expression Python fonctionne, pas seulement une variable.

`f"{prenom=}"` est très pratique pour déboguer : il affiche le nom de la variable suivi de sa valeur, avec les guillemets (`repr`).

Le format après `:` suit la mini-syntaxe de format : `.2f` pour deux décimales, `>10` pour aligner à droite sur 10 caractères.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 04

**Les idiomes Python : slicing**

* Un slice se lit `s[debut:fin:pas]`. La fin n'est pas incluse.
* Les index négatifs comptent depuis la fin.

```python
s = "Python"

print(s[0])     # P
print(s[-1])    # n
print(s[0:2])   # Py
print(s[2:])    # thon
print(s[::2])   # Pto
print(s[::-1])  # nohtyP
```

<!-- .element: class="big-code" -->

Notes:
Le slicing fonctionne sur toutes les séquences : chaînes, listes, tuples. Il crée une nouvelle séquence, sans modifier l'originale.

`s[::-1]` est l'idiome pour inverser : pas de `-1`, donc on parcourt la séquence à l'envers. C'est ce qui permet d'écrire un palindrome en une ligne, comme dans la slide sur les fonctions.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 04

**Les idiomes Python : unpacking et enumerate**

* `premier, *reste = ...` déballe une séquence ; `*reste` récupère « le reste » sous forme de liste.
* `enumerate` donne l'index et la valeur, `zip` parcourt plusieurs séquences en parallèle.

```python
premier, *reste = [1, 2, 3, 4]
print(premier, reste)  # 1 [2, 3, 4]

fruits = ["pomme", "poire", "figue"]
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)  # 1 pomme, 2 poire, 3 figue

for nom, age in zip(["Ada", "Alan"], [36, 41]):
    print(f"{nom} a {age} ans")
```

<!-- .element: class="medium-code" -->

Notes:
Le nombre de variables doit correspondre au nombre d'éléments, sauf avec une étoile : une seule variable préfixée par `*` récupère tous les éléments restants, toujours sous forme de liste, même vide. C'est le même mécanisme que l'échange `x, y = y, x` vu précédemment, et celui des valeurs retournées par une fonction.

Pour parcourir une liste avec son index, on évite `for i in range(len(fruits))` : `enumerate` est plus lisible et moins sujet aux erreurs. Dans `for i, fruit in enumerate(...)`, c'est justement du unpacking : chaque tour déballe un couple (index, valeur).

`zip` s'arrête à la séquence la plus courte. Si les longueurs peuvent différer, c'est un point d'attention.
