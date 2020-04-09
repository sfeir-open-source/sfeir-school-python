<!-- .slide: -->

# Bonnes pratiques - 15

**Pylint - comment imposer ces règles ?**

* Pylint : outils qui permet de faire de l’analyse statique de code :
  * Erreur d’importation
  * Convention de nommage non respectée

* Pour cela, il attribue une note au code, les messages sont classés ainsi :
  * [R]efactor : ne respecte pas les bonnes pratiques
  * [C]onvention : ne respecte pas les conventions de nommage
  * [W]arning : problème de style ou erreur mineure de programmation
  * [E]rror : erreur majeure de programmation (sûrement un bug)
  * [F]atal : impossible de continuer l’analyse

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Bonnes pratiques - 15

**Pylint - un cas d’exemple**

##--##

<br><br>

```python
def main():
  """Main function"""
  list_of_printers = []

  for i in [1, 2, 3]:
    def printer():
      """Print function"""
      print i

    list_of_printers.append(printer)
```

##--##

<br><br>

```python
for func in list_of_printers:
  func()

# 3
# 3
# 3

W: 10,12: Cell variable i defined in loop (cell-var-from-loop)
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Bonnes pratiques - 15

**Pylint - un cas d’exemple**

##--##

<br><br>

```python
def main():
  """Main function"""
  list_of_printers = []

  for i in [1, 2, 3]:
    def make_printer(i):
      """Make printer function"""
      def printer():
        """Print function"""
        print i
      return printer

    list_of_printers.append(make_printer(i))
```

##--##

<br><br>

```python
for func in list_of_printers:
  func()

# 1
# 2
# 3
```
