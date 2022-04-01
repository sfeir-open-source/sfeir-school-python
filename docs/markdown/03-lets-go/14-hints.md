<!-- .slide: -->
# Keep in section lets go ?
# Pour aller plus loin - 13

**Les Hints**

* Une fonction qui prend des paramètres peut typer ses paramètres et son retour.

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 13

**Les Hint**

* Un exemple sans hint :

```python
def is_palindrome(s):
  return s == s[::-1]
```

<!-- .element: class="big-code" -->
* La même méthode avec les hints: 

```python
def is_palindrome(s: str) -> bool:
  return s == s[::-1]
```

<!-- .element: class="big-code" -->
##==##

# Pour aller plus loin - 13

**Les Hint**

- Si s peut être vide

### Python 3.9
```python

def is_palindrome(s: Optional[str] = None) -> bool:
  if s is None:
    return False
  return s == s[::-1]

```
<!-- .element: class="big-code" -->

### Python 3.10
```python

def is_palindrome(s: str | None = None) -> bool:
  if s is None:
    return False
  return s == s[::-1]
```

<!-- .element: class="big-code" -->


Notes:
Permet a l'IDE de connaitre le type attendu. Affiche un warning si le type n'est pas string ou si s peut être null.
Les hints viennent de la librairie standard typing
##==##
<!-- .slide: -->
