<!-- .slide: -->

# Pour aller plus loin - 05

**Les classes**

* Python est orienté objet : une classe décrit une structure et des comportements
* Une **classe** est le modèle, un **objet** (instance) en est une réalisation
* Les méthodes **dunder** (`__nom__`) personnalisent le comportement de Python : `__init__`, `__repr__`, `__str__`, `__add__`...
* On les appelle rarement directement : on écrit `a + b`, pas `a.__add__(b)`

Notes:
Une classe partage des propriétés et des méthodes. `Giraffe` est la classe, `maya = Giraffe(...)` est l'objet.
Les méthodes dunder (double underscore) sont appelées par Python dans certaines situations : `__init__` à la création, `__str__` pour `print`, `__add__` pour `+`. C'est ainsi qu'une classe devient naturelle à utiliser.
Depuis Python 3, toutes les classes héritent implicitement de `object` : on n'écrit plus `class X(object)`.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**Les classes : déclaration et `__init__`**

```python
class Giraffe:
    def __init__(self, name):
        self.name = name

    def drink(self):
        print(f"{self.name} boit.")

maya = Giraffe("Maya")
maya.drink()  # Maya boit.
```

<!-- .element: class="big-code" -->

Notes:
`self` est l'objet courant. C'est le premier paramètre de chaque méthode d'instance, et Python le passe automatiquement : `maya.drink()` équivaut à `Giraffe.drink(maya)`.
`__init__` initialise l'objet. Lors de `Giraffe("Maya")`, Python crée l'objet puis appelle `__init__` ; en pratique, on ne touche qu'à `__init__`.
Les f-strings (`f"..."`) remplacent `.format()`.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**Les classes : héritage**

* Une classe fille reprend les méthodes de sa parente, et peut les spécialiser
* `super()` appelle la méthode de la classe parente

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Giraffe(Animal):
    def __init__(self, name, height):
        super().__init__(name)  # initialise la partie Animal
        self.height = height

maya = Giraffe("Maya", 5)
print(maya.name, maya.height)  # Maya 5
```

<!-- .element: class="medium-code" -->

Notes:
Sans `super().__init__(name)`, l'attribut `name` ne serait jamais défini : la partie héritée reste non initialisée.
Une classe peut hériter de plusieurs classes : `class X(A, B)`. Python suit alors l'ordre MRO (Method Resolution Order), visible avec `X.__mro__`.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**Les classes : `@property`**

* Une méthode utilisée comme un attribut (sans parenthèses), avec de la logique à la lecture ou à l'écriture

```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0  # passe par le setter ci-dessous

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not 0 <= value <= 200:  # validation avant de stocker
            raise ValueError(f"âge invalide : {value}")
        self._age = value  # rangé dans _age, car age est le nom de la propriété

maya = Animal("Maya")
maya.age = 10  # OK
maya.age = 500  # ValueError : âge invalide : 500 (sans @property, ça passerait)
```

<!-- .element: class="medium-code" -->

Notes:
Sans `@property`, `age` serait un simple attribut : `maya.age = 500` passerait sans erreur, personne ne vérifie la valeur.

Avec `@property`, la lecture `maya.age` appelle la méthode décorée (le getter), et l'écriture `maya.age = 10` appelle `@age.setter`, qui peut valider la valeur avant de la stocker. Le code appelant garde la syntaxe d'un attribut ordinaire : on peut commencer avec un attribut simple et ajouter la validation plus tard, sans modifier le code qui utilise la classe. C'est l'équivalent des `get_age()` / `set_age()` de Java, avec une syntaxe plus simple. Sans le setter, l'écriture `maya.age = 10` lèverait `AttributeError` (propriété en lecture seule).

La valeur est stockée dans `self._age`. Un seul underscore signale un attribut interne, par convention. Il faut un autre nom que `age`, sinon le setter se rappellerait lui-même en boucle. On évite `self.__age` : le double underscore déclenche le name mangling (l'attribut devient `_Animal__age`), ce qui n'apporte rien ici et complique l'héritage.
`not 0 <= value <= 200` utilise le chaînage de comparaisons.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**Les classes - classmethod**

* @classmethod : reçoit la classe en 1er paramètre (cls). 
* Utile pour les "factory" qui fonctionnent avec l'héritage, pour faire des constructeurs alternatifs.
```python
import json

class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def from_file(cls, filename):
    # Crée une instance à partir d'un fichier JSON
    # Le fichier animal.json contiendrait : ["Maya", 5]
    with open(filename) as f:
        data = json.load(f)
        return cls(*data)

maya = Animal('Maya', 5) # constructeur normal
maya_from_file = Animal.from_file('animal.json') # alternate constructor
```

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**Les classes - staticmethod**

* @staticmethod : Fonction utilitaire liée à la classe.

```python
from datetime import date
class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @staticmethod
  def get_age_from_year(year):
    return date.today().year - year

age = Animal.get_age_from_year(2000)  # 18
```

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**Les classes : `__repr__` et `__str__`**

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Animal({self.name!r}, {self.age!r})"

    def __str__(self):
        return f"{self.name} : {self.age} ans"

maya = Animal("Maya", 20)
print(maya)    # Maya : 20 ans
print([maya])  # [Animal('Maya', 20)]
```

<!-- .element: class="medium-code" -->

Notes:
`__str__` s'adresse à l'utilisateur : `print()` et `str()` l'appellent.
`__repr__` s'adresse au développeur : le REPL, le debugger et l'affichage d'une liste l'utilisent. Une bonne `repr` permet de reconstruire l'objet à l'identique.
`!r` dans un f-string applique `repr()` à la valeur : les chaînes sont alors entre guillemets.

##==##

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 05

**Les classes - surcharge des opérateurs**

```python
class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __add__(self, animal):  # +
    return Animal(
      '{} + {}'.format(self.name, animal.name),
      self.age + animal.age
    )

  def __sub__(self, animal): pass  #  -
  def __mul__(self, animal): pass  #  *
  def __div__(self, animal): pass  # /
  def __mod__(self, animal): pass  # %
  def __pow__(self, animal): pass  # **
  def __lshift__(self, animal): pass  # <<
  def __rshift__(self, animal): pass  # >>
  def __and__(self, animal): pass  # &
  def __or__(self, animal): pass  # |

  def __str__(self):
    return '{}: {} years old'.format(self.name, self.age)
```

##++##

##++## class="with-code"

<br><br><br><br><br>

```python
a = Animal('Maya', 10)
b = Animal('Jojo', 20)

print(a)  # Maya: 10 years old
print(b)  # Jojo: 20 years old
print(a + b)  # Maya + Jojo: 30 years old
```

##++##

Notes:
N.B. : il est également possible de surcharger les opérateurs de comparaison.
