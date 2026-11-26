<!-- .slide: class="with-code" -->

# Pour aller plus loin - 06

**`@dataclass` : une classe sans le code répétitif**

* Génère `__init__`, `__repr__` et `__eq__` à partir des annotations

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(p)                         # Person(name='Alice', age=30)
print(p == Person("Alice", 30))  # True
```

<!-- .element: class="medium-code" -->

Notes:
Sans `@dataclass`, il faudrait écrire `__init__`, `__repr__` et `__eq__` à la main. Le décorateur les génère à partir des annotations de classe.
Une dataclass reste une classe : on peut y ajouter une `@property`, un `@classmethod`, ou une méthode `__str__`. C'est ce que fait l'exercice 3 du lab step-03.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 06

**Pydantic `BaseModel`**

* Pydantic `BaseModel` = une dataclass qui **valide** ses données à l'exécution
* Même style d'écriture, avec conversion et erreur explicite

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

print(Person(name="Alice", age="30"))  # name='Alice' age=30
Person(name="Bob", age="beaucoup")     # lève ValidationError
```

<!-- .element: class="big-code" -->

Notes:
Pydantic lit les annotations comme `@dataclass`, mais contrôle les données au moment de la création : `age="30"` est converti en entier, `age="beaucoup"` lève `ValidationError`.
C'est exactement ce dont FastAPI a besoin : le JSON reçu par une route est validé par un `BaseModel`, et la réponse est produite à partir du même modèle. On le verra au bloc 5.
Ce qu'on gagne par rapport à la dataclass : la validation et la conversion. Le prix : une dépendance supplémentaire et un léger coût à la création de l'objet.
