<!-- .slide: -->

# Pour aller plus loin - 06

**Les classes**

* Python est aussi un langage orienté objet.
* Petit rappel, il faut bien faire la différence entre :
  * une classe : structure partageant des propriétés
  * un objet : une instance de la classe

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
```

<!-- .element: class="big-code" -->
Notes: On peut hériter de plusieurs classes

##==##
<!-- .slide: class="with-code" -->

<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 06

**Les classes - getter / setter**

##--##

<br><br>

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

##--##

<br><br>

```python
a = Animal('Maya')

a.age = 10
print(a.age)  # 10

a.age = 500  # Maya is too old!
print(a.age)  # 10
```

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 06

**Les classes - classmethod**

```python
class Animal(object):
  max_age = 200
  def __init__(self, name):
    self.name = name
  @classmethod
  def display_max_age(cls):
    print('Animal max age is: {}'.format(cls.max_age))

g = Animal('Maya')
g.display_max_age()
Animal.display_max_age()
```

<!-- .element: class="big-code" -->

Notes:
On peut accéder à une variable de classe avec une classmethod.

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 06

**Les classes - staticmethod**

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

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 06

**Les classes - classmethod vs staticmethod**

##--##

<br><br>

```python
from datetime import date

class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def from_year(cls, name, year):
    return cls(name, date.today().year - year)

  @staticmethod
  def from_name(name):
    return Animal(name, 0)
```

##--##

<br><br>

```python
class Giraffe(Animal):
  pass

a = Giraffe.from_year('Maya', 2017)
print(isinstance(a, Giraffe))  # True

b = Giraffe.from_name('Maya')
print(isinstance(b, Giraffe))  # False
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 06

**Les classes - représentation**

##--##

<br><br>

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

##--##

<br><br>

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

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 06

**Les classes - surcharge des opérateurs**

##--##

<br><br>

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

##--##

<br><br>

```python
a = Animal('Maya', 10)
b = Animal('Jojo', 20)

print(a)  # Maya: 10 years old
print(b)  # Jojo: 20 years old
print(a + b)  # Maya + Jojo: 30 years old
```

Notes:
N.B. : il est également possible de surcharger les opérateurs de comparaison.

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 06

**Les classes - conversion**

##--##

<br><br>

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

##--##

<br><br>

```python
a = Animal('Maya', 2)
l = [10, 20, 30, 40, 50]

print(int(a))  # 2
print(float(a))  # 2.0
print(str(a))  # Maya
print(l[a])  # 30
```
