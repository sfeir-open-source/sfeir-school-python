<!-- .slide: -->

# Pour aller plus loin - 06

**Les classes**

- Python est aussi un langage orienté objet.
- Petit rappel, il faut bien faire la différence entre :
  - une classe : structure partageant des propriétés
  - un objet : une instance de la classe

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 06

**Les classes**

```python
class Giraffe(object):
  def drink(self):
    print('The giraffe is drinking.')

  def eat(self):
    print('The giraffe is eating.')

maya = Giraffe()
maya.drink()
maya.eat()
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: -->

# Pour aller plus loin - 06

**Les classes - méthodes spéciales (dunder)**

- Les méthodes avec des noms qui commencent et se terminent par un double underscore sont appelées "méthodes spéciales" ou "méthodes magiques".
- On les appelle aussi "dunder methods" (de l'anglais double underscore).
- Elles permettent de surcharger le **comportement** par défaut de Python.
  -  `__init__` pour l'initialisation d'objet.
  -  `__add__` pour l'opérateur +.
  -  `__repr__` pour la représentation de l'objet.
- On ne les appelle généralement pas directement (ex: a + b au lieu de a.__add__(b)).

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 06

**Les classes - constructeur**

```python
class Giraffe(object):
  def __init__(self, name):
    self.name = name

  def drink(self):
    print('{} is drinking.'.format(self.name))

  def eat(self):
    print('{} is eating.'.format(self.name))

maya = Giraffe('Maya') 
```

<!-- .element: class="big-code" -->

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 06

**Les classes - héritage**

```python
class Animal(object):
  def __init__(self, name):
    self.name = name
  def drink(self):
    print('{} is drinking.'.format(self.name))
  def eat(self):
    print('{} is eating.'.format(self.name))
class Giraffe(Animal):
  def eat_leaves(self):
    print('{} is eating some leaves.'.format(self.name))
maya = Giraffe('Maya')
maya.drink() # nous pouvons utiliser les méthodes de la classe parente
maya.eat() # idem
maya.eat_leaves() # "spécialisation" d'une Giraffe par rapport à un Animal.
```

Notes: On peut hériter de plusieurs classes

##==##

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 06

**Les classes - getter / setter**

<br>

```python
class Animal(object):
  max_age = 200
  def __init__(self, name):
    self.name = name
    self.age = 0

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, age):
    if age <= Animal.max_age:
      self.__age = age
    else:
      print('{} is too old!'.format(self.name))
```

##++##

##++## class="with-code"

<br><br><br><br><br><br>

```python
a = Animal('Maya')

a.age = 10
print(a.age)  # 10

a.age = 500  # Maya is too old!
print(a.age)  # 10
```

##++##

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 06

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

# Pour aller plus loin - 06

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

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 06

**Les classes - représentation**

<br>

```python
class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return '{}({}, {})'.format(
      self.__class__.__name__,
      repr(self.name),
      repr(self.age))

  def __str__(self):
    return '{}: {} years old'.format(self.name, self.age)
```

##++##

##++## class="with-code"

<br><br><br><br><br><br>

```python
a = Animal('Maya', 20)
b = Animal('Jojo', 100)

print(a)
# Avant  <__main__.Animal object at 0x103476bd0>

# Apres - Maya: 20 years old

print([a, b])
# Avant - [<__main__.Animal object at 0x103476bd0>, <__main__.Animal object at 0x103476c10>]

# Apres - [Animal('Maya', 20), Animal('Jojo', 100)]
```

##++##

##==##

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 06

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
##==##

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 06

**Les classes - conversion**

<br>

```python
class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __float__(self):
    return float(self.age)

  def __index__(self):
    return int(self.age)

  def __int__(self):
    return self.age

  def __str__(self):
    return self.name
```

##++##

##++## class="with-code"

<br><br><br><br><br><br>

```python
a = Animal('Maya', 2)
l = [10, 20, 30, 40, 50]

print(int(a))  # 2
print(float(a))  # 2.0
print(str(a))  # Maya
print(l[a])  # 30
```

##++##
