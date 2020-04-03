<!-- .slide: -->

# Les bases - 09

**Les exceptions**

* Une exception est une erreur qui met fin au programme.
* Toutes les exceptions ont pour classe parente “BaseException”.
* Il y a 4 grandes classes d’exception :
  * SystemExit : à l’appel de “sys.exit” ; pas de stacktrace
  * KeyboardInterrupt : interruption du programme
  * GeneratorExit : méthode “close” du générateur
  * Exception : les erreurs générées par le programme

##==##
<!-- .slide: -->

# Les bases - 09

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

# Les bases - 09

**Les exceptions**

* C’est le mécanisme usuel pour renvoyer une erreur.
* Il est courant de déclarer sa propre exception :

```python
class MyCustomException(Exception):
  pass
```

<!-- .element: class="big-code" -->

<br>

* Cela permet de faciliter la gestion d’erreur.

##==##
<!-- .slide: class="with-code" -->

# Les bases - 09

**Les exceptions**

```python
try:
  return animals[100 / i]

except (IndexError, ZeroDivisionError):
  return None

except KeyError:
  pass  # "animals" is a dict?
  
finally:
  print 'always executed'
```

<!-- .element: class="big-code" -->
