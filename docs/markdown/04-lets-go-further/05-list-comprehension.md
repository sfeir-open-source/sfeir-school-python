<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**La list comprehension**

* C’est une manière de créer une liste à partir d’un itérable.
* Elle doit au minimum contenir une clause “for”.

```python
result = [x for x in iterable ... if condition ...]
```

<!-- .element: class="big-code" -->

* Il peut y avoir plusieurs boucles et plusieurs conditions.

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 05

**La list comprehension**

* Comment remplacer le code suivant avec une list comprehension ?

##--##

<br><br><br>

```python
letters = []

for letter in 'chaine':
  letters.append(letter)
```

##--##

<br><br><br>

```python
print(letters)

# ['c', 'h', 'a', 'i', 'n', 'e']
```

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**La list comprehension**

* Comment remplacer le code suivant avec une list comprehension ?

```python
letters = [letter for letter in 'chaine']
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 05

**La list comprehension**

* Set comprehension

```python
letters = {letter for letter in 'aaaaaab' if letter == "a"}
# print(letters) => set(['a'])
```

<!-- .element: class="big-code" -->