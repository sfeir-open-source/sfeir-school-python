<!-- .slide: -->

# Pour aller plus loin - 03

**Les décorateurs**

* Un décorateur est une fonction qui permet de modifier le comportement d’une autre fonction ou d’une classe.
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
import time
def timer(func):
  def wrapper():
    start_time = time.time()
    result = func()
    end_time = time.time()
    print(f"'{func.__name__}' a mis {end_time - start_time:.4f}s")
    return result
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
import time
@timer
def calcul_long(duree=2):
  """Simule un traitement qui prend du temps."""
  return time.sleep(duree)
```
```
>>> calcul_long()
'calcul_long' a mis 2.0051s
>>> calcul_long(3)
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    calcul_long(3)
    ~~~~~~~~~~~^^^
TypeError: timer.<locals>.wrapper() takes 0 positional arguments but 1 was given
```

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Les décorateurs**

* Comment gérer le passage des arguments ?

```python
import time

def timer(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"'{func.__name__}' a mis {end_time - start_time:.4f}s")
    return result
  return wrapper
```
```
>>> calcul_long(3)
'calcul_long' a mis 3.0051s
```

<!-- .element: class="big-code" -->
