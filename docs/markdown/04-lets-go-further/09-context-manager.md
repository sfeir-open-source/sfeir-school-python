<!-- .slide: -->

# Pour aller plus loin - 06

**Les classes - context manager**

- C’est généralement une classe.
- On l’utilise avec le mot clé “with”.
- Permet de visualiser la portion de code concernée.
- Permet de réutiliser les actions faites à l’entrée et à la sortie.
- L’action de sortie est toujours exécutée même en cas d’exception (correspond globalement au mot clé “finally”).

##==##

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 07

**Les classes - context manager**

<br>

```python
class MyContextManager(object):
  def __enter__(self):
    print("Before")

  def __exit__(self):
    print("After")
```

##++##

##++## class="with-code"

<br><br><br><br><br><br>

```python
with MyContextManager():
  print("func")

# Before
# func
# After
```

##++##

##==##

<!-- .slide: class="with-code tc-multiple-columns" -->

##++##

# Pour aller plus loin - 07

**Les classes - context manager**

<br>
Sans context manager:

```python
import os

file = open(file_path, mode='r')
# Reading the file line by line.
line = file.readlines() # Read line one by one
while line:
    print(line)
    line = file.readline()
file.close() # Close file
```

##++##

##++## class="with-code"

<br><br><br><br><br><br>

Avec context manager:

```python
with open(file_path, mode='r') as file: # Open and Close file
  # Reading the file line by line.
  line = file.readlines() # Read line one by one
  while line:
    print(line)
    line = file.readline()
```

##++##
