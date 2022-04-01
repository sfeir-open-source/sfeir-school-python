<!-- .slide: -->

# Pour aller plus loin - 03

**Les décorateurs**

* Un décorateur est une fonction qui permet de modifier le comportement d’une autre fonction ou d’une classe.
* Ainsi c’est le décorateur qui choisit d’appeler la fonction ou non.
* Avantages :
  * Lisibilité
  * Réutilisation
  * Modularité

Notes:
Lisibilité : une partie de la la logique du code est déportée hors de la fonction

Réutilisation : permet de réutiliser un comportement ou une logique à plusieurs endroits (ex. : gestion de droits d’une API)

Modularité : permet d’organiser son code en conséquence et de le partager ainsi plus facilement

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Les décorateurs**

* Le décorateur doit retourner une fonction : le wrapper.

```python
def mon_decorateur(func):
  def wrapper():
    print 'avant'
    res = func()
    print 'après'

    return res
  return wrapper
```

<!-- .element: class="big-code" -->

Notes:
Le wrapper : fonction qui enveloppe généralement la fonction initiale

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Les décorateurs**

* Comment utiliser le décorateur ?

```python
@mon_decorateur
def is_palindrome(s='hello'):
  """Indique si la chaine s est un palindrome"""
  return s == s[::-1]

mon_decorateur(is_palindrome)()  # sans le décorateur
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Les décorateurs**

* Comment gérer le passage des arguments ?

```python
def mon_decorateur(func):
  def wrapper(*args, **kwargs):
    print 'avant'
    res = func(*args, **kwargs)
    print 'après'

    return res
  return wrapper
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Les décorateurs**

* Comment rendre un décorateur paramétrable ?

```python
def mon_super_decorateur(call=True):
  def mon_decorateur(func):
    def wrapper(*args, **kwargs):
      if call:
        return func(*args, **kwargs)

    return wrapper
  return mon_decorateur
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Les décorateurs**

* Comment l’utiliser ?

```python
@mon_super_decorateur()
@mon_super_decorateur(call=False)
```

<!-- .element: class="big-code" -->

<br>

* équivalent à :

```python
mon_super_decorateur(True)(is_palindrome)()
```

<!-- .element: class="big-code" -->