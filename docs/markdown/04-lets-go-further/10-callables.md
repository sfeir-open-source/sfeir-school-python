<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - callable (comme une fonction)**

##--##

<br><br>

```python
class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __call__(self):
    print('Hello {} ({} years old)!'.format(
      self.name,
      self.age
    ))
```

##--##

<br><br>

```python
a = Animal('Maya', 20)
a()  # Hello Maya (20 years old)!
```
