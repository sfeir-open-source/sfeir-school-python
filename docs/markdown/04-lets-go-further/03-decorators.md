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

* Le décorateur renvoie une fonction : le `wrapper`, qui enveloppe la fonction d'origine

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
`func` est la fonction décorée. Le `wrapper` la capture et s'en souvient après la fin de `timer` : c'est une fermeture (closure).
`time.perf_counter()` est l'horloge prévue pour mesurer une durée. `time.time()` donne l'heure murale, qui peut être recalée par le réseau (NTP) pendant la mesure.
Cette version ne fonctionne que pour les fonctions sans argument. La slide suivante le montre.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Les décorateurs**

* Utilisation avec `@timer` :

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

**Les décorateurs : arguments et `functools.wraps`**

```python
import functools
import time

def timer(func):
    @functools.wraps(func)                     # garde le nom et la docstring de func
    def wrapper(*args, **kwargs):              # accepte tous les arguments...
        start = time.perf_counter()
        result = func(*args, **kwargs)         # ...et les transmet tels quels
        print(f"'{func.__name__}' a mis {time.perf_counter() - start:.4f} s")
        return result
    return wrapper

@timer
def additionner(a, b):
    """Additionne deux nombres."""
    return a + b

print(additionner(2, b=3))     # 'additionner' a mis 0.0000 s, puis 5
print(additionner.__name__)    # additionner (sans wraps : wrapper)
```

<!-- .element: class="medium-code" -->

Notes:
`*args` et `**kwargs` acceptent n'importe quels arguments et les transmettent tels quels à `func`. Le `wrapper` est transparent pour l'appelant.
`@functools.wraps(func)` copie le nom, la docstring et le module de `func` dans le `wrapper`. Sans lui, `calcul_long.__name__` vaudrait `"wrapper"`, et `help(calcul_long)` n'afficherait plus la docstring.
Ce n'est pas un détail : FastAPI, par exemple, lit la signature et la documentation des fonctions. Dès qu'on décore une fonction, on utilise `wraps`.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 03

**Décorateurs utiles de la stdlib**

* `@functools.cache` : mémorise les résultats (memoization)
* `@property` : une méthode lue comme un attribut (cf. classes)
* `@classmethod` : reçoit la classe en paramètre (cf. classes)
* `@dataclass` : génère `__init__`, `__repr__` et `__eq__` (cf. dataclasses)

```python
import functools

@functools.cache
def fibonacci(n: int) -> int:
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(80))  # 23416728348467685, instantané grâce au cache
```

<!-- .element: class="medium-code" -->

Notes:
Sans `@functools.cache`, `fibonacci(80)` recalcule les mêmes valeurs des milliards de fois. Avec le cache, chaque valeur est calculée une seule fois.
Décorateur paramétré, par exemple `@repeat(3)`. La fonction extérieure reçoit le paramètre et renvoie le décorateur, il y a donc un niveau d'imbrication de plus.
Ces décorateurs de la stdlib sont ceux qu'on rencontre le plus. `property`, `classmethod` et `dataclass` sont détaillés dans les slides suivantes.
