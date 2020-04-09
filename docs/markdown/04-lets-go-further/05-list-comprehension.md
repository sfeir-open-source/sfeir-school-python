<!-- .slide: class="with-code" -->

# Pour aller plus loin - 13

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

# Pour aller plus loin - 13

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

# Pour aller plus loin - 13

**La list comprehension**

* Comment remplacer le code suivant avec une list comprehension ?

```python
letters = [letter for letter in 'chaine']
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 13

**La list comprehension**

* Avec plusieurs boucles.

```python
[x + y for x in [1, 2, 3] for y in [10, 20, 30]]

# [11, 21, 31, 12, 22, 32, 13, 23, 33]
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 13

**La list comprehension**

* Avec plusieurs boucles et plusieurs conditions.

```python
[x + y for x in [1, 2, 3] for y in [10, 20, 30] if (x+y)%11 == 0]
# [11, 22, 33]

[x + y for x in [1, 2, 3] for y in [10, 20, 30] if (x+y)%11 == 0 if (x+y)%2 == 0]
# [22]
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 13

**La list comprehension**

* Set comprehension

```python
letters = {letter for letter in 'aaaaaab'}
# print(letters) => set(['a', 'b'])
```

<!-- .element: class="big-code" -->

<br>

* Generator comprehension

```python
letters = (letter for letter in 'chaine')
# print(letters) => generator
# print(list(letters)) => ['c', 'h', a', 'i', 'n', 'e']
```

<!-- .element: class="big-code" -->

Notes:
La syntaxe ne change pas !
