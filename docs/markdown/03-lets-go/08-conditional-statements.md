<!-- .slide: class="with-code" -->

# Les bases - 07

**Les conditions**

* La déclaration `if` en Python s'écrit sans parenthèses :

```python
condition = True
if condition:
    pass
```

<!-- .element: class="big-code" -->

<br>

* Comme pour les fonctions, la ligne se finit par le caractère `:`.

Notes:
Parler des mots-clés `pass` (instruction vide, utile comme espace réservé) et `del` (suppression d'une variable ou d'un élément).

##==##

<!-- .slide: -->

# Les bases - 07

**Les conditions**

* La condition est une expression booléenne.
* Nous retrouvons les opérateurs classiques :

|               |                       |                    |           |
|---------------|-----------------------|--------------------|-----------|
| **`<`**       | strictly less than    | **`==`**           | equal     |
| **`<=`**      | less than or equal    | **`!=`**           | not equal |
| **`>`**       | strictly greater than | `x` **`or`** `y`   | or        |
| **`>=`**      | greater than or equal | `x` **`and`** `y`  | and       |
| **`not`** `a` | not                   |                    |           |

##==##

<!-- .slide: class="with-code" -->

# Les bases - 07

**Les conditions**

* La clause « **else** » s'utilise de façon classique, et les « **elif** » s'enchaînent.

```python
condition1 = False
condition2 = True
if condition1:
    print('c1')
elif condition2:
    print('c2')
else:
    print('c3')
```

<!-- .element: class="big-code" -->

Notes:
Python n'a pas d'instruction `switch` ; pour un choix sur une même valeur, on enchaînait des `elif`, ou on utilisait un dictionnaire. Depuis Python 3.10, `match` (slide suivante) fait ce travail.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 07

**Les conditions**

* Une ternaire est une condition sur une ligne.

```python
value = 42
is_positive = True if value >= 0 else False
```

<!-- .element: class="big-code" -->

Notes:
La ternaire s'écrit `valeur_si_vrai if condition else valeur_si_faux`. Elle est pratique pour une affectation simple. Dès que la logique se complique, un `if` classique reste plus lisible.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 07

**Les conditions : `match`**

* Depuis Python 3.10, `match` remplace une suite de `elif` sur une même valeur.
* `|` teste plusieurs valeurs, `_` est le cas par défaut.

```python
status = 404

match status:
    case 400:
        print("Bad request")
    case 401 | 403 | 404:
        print("Not allowed")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")
```

<!-- .element: class="medium-code" -->

Notes:
Pas de `switch` en Python, mais `match` joue ce rôle. Chaque `case` est un motif (pattern) comparé à la valeur, dans l'ordre : le premier motif qui correspond est exécuté, et les suivants sont ignorés. Pas besoin de `break`, donc pas de « fall-through » comme dans le `switch` de Java ou de JavaScript.

Pour des valeurs littérales comme ici, la comparaison revient à une égalité. La slide suivante montre ce que `match` fait de plus.
