<!-- .slide: -->

# Orienté Objet - 14

**Les classes - context manager**

* C’est généralement une classe.
* On l’utilise avec le mot clé “with”.
* Permet de visualiser la portion de code concernée.
* Permet de réutiliser les actions faites à l’entrée et à la sortie.
* L’action de sortie est toujours exécutée même en cas d’exception (correspond globalement au mot clé “finally”).

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - context manager**

##--##

<br><br>

```python
class MyContextManager(object):
  def __enter__(self):
    print 'Before'

  def __exit__(
    self,
    type,
    value,
    traceback
  ):
    print 'After'
    print type
    print value
    print traceback
```

##--##

<br><br>

```python
# Before
# After

# <type 'exceptions.Exception'>
# Oups
# <traceback object at 0x1047a4128>
# Traceback (most recent call last):
#   File "example.py", line 12, in <module>
#     raise Exception('Oups')
# Exception: Oups
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Orienté Objet - 14

**Les classes - context manager**

##--##

<br><br>

```python
import os

class Cd(object):
  def __init__(self, dir_name):
    self.dir_name = dir_name

  def __enter__(self):
    self.current_dir = os.getcwd()
    os.chdir(self.dir_name)

  def __exit__(self, type, value, traceback):
    os.chdir(self.current_dir)
```

##--##

<br><br>

```python
# /home/user/project

with Cd('/tmp'):
  # /tmp

  with Cd('/tmp/foo'):
    # /tmp/foo
    pass

  # /tmp

# /home/user/project
```
