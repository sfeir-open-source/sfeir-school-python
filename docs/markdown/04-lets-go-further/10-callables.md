<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 08

**Les classes - callable**

* Rendre un objet "appelable" comme une fonction.
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

##++##

##++## class="with-code"

<br><br><br><br><br><br><br><br>

```python
a = Animal('Maya', 20)
a()  # Hello Maya (20 years old)!
```

##++##
