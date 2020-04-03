<!-- .slide: class="with-code" -->

# Les bases - 03

**Opérations sur les dictionnaires**

```python
a = {'key1': 'abc', 'key2': 'xyz'}
a.keys() // a.values()  # ['key2', 'key1'] // ['xyz', 'abc']
a.items()  # [('key2', 'xyz'), ('key1', 'abc')]
a.iterkeys() // a.itervalues()  # iterator
a.iteritems()  # iterator

'key1' in a  # True
a['key1'] // a.get('key1') // a.get('key3', 'abc')  # abc
```

<!-- .element: class="big-code" -->

Notes:
Rappel : les dictionnaires ne sont pas ordonnés.

##==##
<!-- .slide: class="with-code" -->

# Les bases - 03

**Opérations sur les listes**

```python
a = [10, 30, 20]

a[0]  # 10
a[3]  # IndexError: list index out of range
a += '40'  # [10, 30, 20, 4, 0]
a += [40] // a.append(40)  # [10, 30, 20, 40]
a.reverse()  # Ne retourne rien : [20, 30, 10]
reversed(a)  # il faut itérer pour avoir la liste
sorted(a)  # [10, 20, 30]
```

<!-- .element: class="big-code" -->

Notes:
Reversed : générateur, il faut itérer pour avoir la liste

sorted : renvoie la liste triée (pas de générateur)

##==##
<!-- .slide: class="with-code" -->

# Les bases - 03

**Opération sur les sets**

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
```

<!-- .element: class="big-code" -->

![center h-600](./assets/images/set_operations.png)

Notes:
union
intersection
difference
symmetric_difference
…
