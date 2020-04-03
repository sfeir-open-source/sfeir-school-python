<!-- .slide: -->

# Orienté Objet - 14

**Les classes**

* Python est aussi un langage orienté objet.
* Petit rappel, il faut bien faire la différence entre :
  * une classe : structure partageant des propriétés
  * un objet : une instance de la classe

##==##
<!-- .slide: class="with-code" -->

# Orienté Objet - 14

**Les classes**

```python
class Giraffe(object):
  def drink(self):
    print 'The giraffe is drinking.'

  def eat(self):
    print 'The giraffe is eating.'

maya = Giraffe()
maya.drink()
maya.eat()
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Orienté Objet - 14

**Les classes - constructeur**

```python
class Giraffe(object):
  def __init__(self, name):
    self.name = name

  def drink(self):
    print '{} is drinking.'.format(self.name)

  def eat(self):
    print '{} is eating.'.format(self.name)

maya = Giraffe('Maya')
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Orienté Objet - 14

**Les classes - héritage**

```python
class Animal(object):
  def __init__(self, name):
    self.name = name

  def drink(self):
    print '{} is drinking.'.format(self.name)

  def eat(self):
    print '{} is eating.'.format(self.name)

class Giraffe(Animal): pass
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Orienté Objet - 14

**Les classes - héritage**

```python
class Giraffe(Animal):
  def eat_leaves(self):
    print '{} is eating some leaves.'.format(self.name)

class Carnivorous(Animal):
  def __init__(self, name, diet='carnivore'):
    self.diet = diet
    super(Carnivorous, self).__init__(name)

  def display_diet(self):
    print '{} is {}.'.format(self.name, self.diet)
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - héritage multiple**

##--##

<br>

```python
class Hunter(object):
  def hunt(self):
    print '{} is hunting.'.format(self.name)

class Eagle(Carnivorous, Hunter):
  pass
```

##--##

![center h-600](./assets/images/class_diagram.png)

##==##
<!-- .slide: class="with-code" -->

# Orienté Objet - 14

**Polymorphisme**

```python
class Giraffe(Animal):
  def eat(self):
    print 'Giraffe is eating'

class Eagle(Animal):
  def eat(self):
    print 'Eagle is eating'

animals = [Giraffe(), Eagle()]
for a in animals:
  a.eat()
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - getter / setter**

##--##

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
      print '{} is too old!'.format(self.name)
```

##--##

<br>

```python
a = Animal('Maya')

a.age = 10
print a.age  # 10

a.age = 500  # Maya is too old!
print a.age  # 10
```

##==##
<!-- .slide: class="with-code" -->

# Orienté Objet - 14

**Les classes - classmethod**

```python
class Animal(object):
  max_age = 200
  def __init__(self, name):
    self.name = name
  @classmethod
  def display_max_age(cls):
    print 'Animal max age is: {}'.format(cls.max_age)

g = Animal('Maya')
g.display_max_age()
Animal.display_max_age()
```

<!-- .element: class="big-code" -->

Notes:
On peut accéder à une variable de classe avec une classmethod.

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - classmethod**

##--##

<br>

```python
from datetime import date

class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def from_year(cls, name, year):
    return cls(name, date.today().year - year)

  def display(self):
    print "{}'s age: {}".format(self.name, self.age)
```

##--##

<br>

```python
a = Animal('Maya', 10)
a.display()  # Maya's age is 10

b = Animal.from_year('Jojo', 2000)
b.display()  # Jojo's age is 18
```

Notes:
On peut également créer une autre classe avec une classmethod.

##==##
<!-- .slide: class="with-code" -->

# Orienté Objet - 14

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

# Orienté Objet - 14

**Les classes - classmethod vs staticmethod**

##--##

<br>

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

<br>

```python
class Giraffe(Animal):
  pass

a = Giraffe.from_year('Maya', 2017)
print isinstance(a, Giraffe)  # True

b = Giraffe.from_name('Maya')
print isinstance(b, Giraffe)  # False
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - destructeur**

##--##

<br>

```python
import time

class Animal(object):
  def __init__(self, name):
    print 'Hello {}!'.format(name)

  def __del__(self):
    print 'Bye bye!'
```

##--##

<br>

```python
g = Animal('Maya')
# Hello Maya!

del g
# Bye bye!

# Wait for garbage collector
# to destroy the object
time.sleep(1)
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - représentation**

##--##

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

##--##

<br>

```python
a = Animal('Maya', 20)
b = Animal('Jojo', 100)

print a
# Avant  <__main__.Animal object at 0x103476bd0>

# Apres - Maya: 20 years old

print [a, b]
# Avant - [<__main__.Animal object at 0x103476bd0>, <__main__.Animal object at 0x103476c10>]

# Apres - [Animal('Maya', 20), Animal('Jojo', 100)]
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - surcharge des opérateurs**

##--##

<br>

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

<br>

```python
a = Animal('Maya', 10)
b = Animal('Jojo', 20)

print a  # Maya: 10 years old
print b  # Jojo: 20 years old
print a + b  # Maya + Jojo: 30 years old
```

Notes:
N.B. : il est également possible de surcharger les opérateurs de comparaison.

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - conversion**

##--##

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

##--##

<br>

```python
a = Animal('Maya', 2)
l = [10, 20, 30, 40, 50]

print int(a)  # 2
print float(a)  # 2.0
print str(a)  # Maya
print l[a]  # 30
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - programmation dynamique**

##--##

<br>

```python
class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __getattr__(self, attr_name):
    print 'Getting {}...'.format(attr_name)
    return None

  def __setattr__(self, attr_name, attr_value):
    print 'Setting {}...'.format(attr_name)
    super(Animal, self).__setattr__(attr_name, attr_value)

  def __delattr__(self, attr_name):
    print 'Deleting {}...'.format(attr_name)
```

##--##

<br>

```python
a = Animal('Maya', 2)
# Setting name...
# Setting age...

print a.eat  # (attribute does not exists)
# Getting eat...
# None

a.eat = True  # Setting eat...
print a.eat  # True
del a.eat  # Deleting eat...
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - programmation dynamique**

##--##

<br>

```python
class Animal(object):
  def __init__(self, name, age, *args):
    self.name = name
    self.age = age
    self.other_names = list(args)  # args is immutable

  def __len__(self):
    return len(self.other_names)

  def __getitem__(self, key):
    return self.other_names[key]

  def __setitem__(self, key, value):
    self.other_names[key] = value

  def __delitem__(self, key):
    pass

  def __iter__(self):
    return iter(self.other_names)

  def __reversed__(self):
    return reversed(self.other_names)
    
  def __contains__(self, key):
    return key in self.other_names
```

##--##

<br>

```python
a = Animal('Maya', 2, 'Jojo', 'Yoyo', 'Bobo')

a[2] = 'Zozo'
print a[2]  # Zozo
print list(a)  # ['Joyo', 'Yoyo', 'Zozo']
print list(reversed(a))  # ['Zozo', 'Yoyo', 'Jojo']
print 'Jojo' in a  # True
print 'Bobo' in a  # False
```

Notes:
args est une tuple (immutable)
