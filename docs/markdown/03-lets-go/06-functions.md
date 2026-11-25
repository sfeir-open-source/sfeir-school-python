<!-- .slide: class="with-code" -->

# Les bases - 05

**Les fonctions**

* Le corps de la fonction correspond à tout ce qui est indenté sous la ligne `def`.

```python
def is_palindrome():
    pass
```

<!-- .element: class="big-code" -->

##==##

<!-- .slide: class="with-code" -->

# Les bases - 05

**Les fonctions**

* Une fonction peut prendre zéro ou plusieurs arguments.

```python
def is_palindrome(arg1, arg2, arg3):
    pass
```

<!-- .element: class="big-code" -->

<br>

* Python est à **typage dynamique** : les types sont vérifiés à l'exécution. Les annotations de type sont optionnelles, mais elles aident la lecture et les outils.

```python
def is_palindrome(s: str) -> bool:
    pass
```

<!-- .element: class="big-code" -->

##==##

<!-- .slide: class="with-code" -->

# Les bases - 05

**Les fonctions**

* Une fonction peut prendre des arguments par défaut.

* Les paramètres avec valeur par défaut deviennent facultatifs. Pour sauter ceux du milieu, on les **nomme** à l'appel.

```python
def ma_fonction(a, b, c=False, d=None):
    return f"a={a}, b={b}, c={c}, d={d!r}"


print(ma_fonction(10, 42))         # a=10, b=42, c=False, d=None
print(ma_fonction(10, 42, d="x"))  # a=10, b=42, c=False, d='x'
```

<!-- .element: class="big-code" -->

##==##

<!-- .slide: class="with-code" -->

# Les bases - 05

**Les fonctions**

* Une fonction peut retourner une valeur avec `return`. Sans `return`, elle renvoie `None`.

```python
def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("radar"))  # True
```

<!-- .element: class="big-code" -->

##==##

<!-- .slide: class="with-code" -->

# Les bases - 05

**Les fonctions**

* Une fonction peut aussi retourner **plusieurs** valeurs, sous forme de tuple.

```python
def get_xy(s):
    # Exemple : "12.345 -6.789"
    xy = s.split(' ')
    return float(xy[0]), float(xy[1])


x, y = get_xy("12.345 -6.789")  # x = 12.345, y = -6.789
```

<!-- .element: class="big-code" -->

##==##

<!-- .slide: class="with-code" -->

# Les bases - 05

**Les fonctions**

* Les fonctions peuvent aussi prendre un nombre d'arguments indéterminé.

```python
def my_func(*args, **kwargs):
    print(args, kwargs)


my_func(42, "hello", param="world")
# (42, 'hello') {'param': 'world'}
```

<!-- .element: class="big-code" -->

Notes:
`*args` reçoit les arguments positionnels, sous forme de tuple. `**kwargs` reçoit les arguments nommés, sous forme de dictionnaire.

Par convention, les noms de fonctions s'écrivent en `snake_case` : `my_func`, et non `myFunc`. C'est la recommandation PEP 8.
