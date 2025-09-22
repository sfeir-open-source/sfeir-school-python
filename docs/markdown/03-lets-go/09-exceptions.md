<!-- .slide: -->

# Les bases - 08

**Les exceptions**

* Une exception est une erreur qui met fin au programme.
* C’est le mécanisme usuel pour gérer une erreur attendue du programme.
* Toutes les exceptions ont pour classe parente “BaseException”.
* Il y a 4 grandes classes d’exception :
  * `SystemExit`: `sys.exit()`
  * `KeyboardInterrupt`: Ctrl+C
  * `GeneratorExit`: `generator.close()`
  * `Exception`: Erreurs "classiques" (`ValueError`, `TypeError`...)


##==##

<!-- .slide: -->

# Les bases - 08

**Les exceptions**

|         |         |         |
| ------- | ------- | ------- |
| StopIteration | EOFError | RuntimeError |
| ArithmeticError | ImportError | SyntaxError |
| AssertionError | LookupError | SystemError |
| AttributeError | MemoryError | TypeError |
| BufferError | NameError | ValueError |
| EnvironmentError | ReferenceError | Warning |


##==##

<!-- .slide: class="with-code" -->

# Les bases - 08

**Les exceptions**

* Créer ses propres exceptions permet de capturer des erreurs métier spécifiques.

```python
class MyCustomException(Exception):
  pass
```

* Depuis Python 3.11, on peut ajouter des notes pour enrichir le contexte.

```python
try:
    raise TypeError("Oups")
except TypeError as e:
    e.add_note("Information contextuelle supplémentaire")
    raise
```
<!-- .element: class="big-code" -->

<br>

##==##

<!-- .slide: class="with-code" -->

# Les bases - 08

**Les exceptions**

```python
try:
  return animals[100 / i]
except (IndexError, ZeroDivisionError):
  return None
except KeyError:
  pass  # "animals" is a dict?
finally:
  print('always executed')
```

<!-- .element: class="big-code" -->
