<!-- .slide: -->
# Pour aller plus loin - 01

**Typage statique (Type Hints)**

*   Améliore la lisibilité et la robustesse du code.
*   Essentiel pour les IDEs, linters et l'IA (ex: Copilot).

##==##

<!-- .slide: class="with-code" -->
# Pour aller plus loin - 01

**Les Type Hints (annotations de type)**

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

<!-- .slide: class="with-code" -->
# Pour aller plus loin - 01

**Les Type Hints (annotations de type)**

### Depuis Python 3.10
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
