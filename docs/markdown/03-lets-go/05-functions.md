<!-- .slide: class="with-code" -->

# Les bases - 04

**Les fonctions**

* Une fonction est déclarée à l’aide du mot clé **def** suivi du nom de la fonction.
* Le corps de la fonction correspond à tout ce qui est indenté dans le même bloc en-dessous.

```python
def is_palindrome():
  pass
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Les bases - 04

**Les fonctions**

* Une fonction peut prendre zéro ou plusieurs arguments.

```python
def is_palindrome(s):
  pass
```

<!-- .element: class="big-code" -->

<br>

* Python est un langage non typé (mais il existe des hints pour la lisibilité du code).

```python
def is_palindrome(s: str) -> bool:
    pass
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Les bases - 04

**Les fonctions**

* Une fonction peut prendre des arguments par défaut.

```python
def ma_fonction(a, b, c=False, d=None):
  pass
```

<!-- .element: class="big-code" -->

<br>

* Dans ce cas là, les paramètres deviennent facultatifs. Il est possible de n’en renseigner que certains en les nommant.

```python
ma_fonction(10, 42, 'ok')
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Les bases - 04

**Les fonctions**

* Une fonction peut retourner une valeur.

```python
def is_palindrome(s):
  return True
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Les bases - 04

**Les fonctions**

* Une fonction peut aussi retourner **plusieurs** valeurs.

```python
def get_xy(s):
  # 12.345 -6.789
  xy = s.split(' ')
  return float(xy[0]), float(xy[1])
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Les bases - 04

**Les fonctions**

* Les fonctions peuvent aussi prendre un nombre d’arguments indéterminé.

```python
def myFunc(*args, **kwargs):
  print(args, kwargs)

myFunc(42, 'hello', param='world')
# args: (42, 'hello')
# kwargs: {'param': 'world'}
```

<!-- .element: class="big-code" -->
