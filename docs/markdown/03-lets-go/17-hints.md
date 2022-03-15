<!-- .slide: -->

# Pour aller plus loin - 12

**Les Hints**

* Une fonction qui prend des paramètres peut typer ses paramètres.

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 12

**Fonction**

* Un exemple sans hint :

```python
def is_palindrome(s):
  return s == s[::-1]
```

* La même méthode avec les hints: 

```python
def is_palindrome(s: string) -> bool:
  return s == s[::-1]
```

Si s peut être vide
```python
def is_palindrome(s: Optional[string]) -> bool:
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
