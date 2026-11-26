<!-- .slide: class="with-code" -->

# Les bases - 03

**Opérations sur les dictionnaires**

```python
a = {'key1': 'abc', 'key2': 'xyz'}
a.keys()    # dict_keys(['key1', 'key2'])
a.values()  # dict_values(['abc', 'xyz'])
a.items()   # dict_items([('key1', 'abc'), ('key2', 'xyz')])

'key1' in a               # True
a['key1']                 # 'abc'
# a['key3']               # KeyError : la clé n'existe pas
a.get('key3', 'défaut')   # 'défaut' (pas d'erreur)
```

<!-- .element: class="big-code" -->

Notes:
En Python 3, `keys()`, `values()` et `items()` renvoient des **vues** : elles reflètent le dictionnaire en direct, sans copier les données. Elles s'affichent `dict_keys([...])`, pas comme une liste. Elles sont itérables, et on peut tester `in` ou appeler `len()` dessus.

Les méthodes `iterkeys()`, `itervalues()` et `iteritems()` appartenaient à Python 2 : elles n'existent plus en Python 3. Les vues les remplacent.

`a['key3']` lève une `KeyError`. `a.get(...)` renvoie une valeur par défaut à la place, sans erreur.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 03

**Dictionnaires : ordre et fusion**

* Ordre d'insertion conservé (garanti depuis Python 3.7).
* `a | b` fusionne deux dictionnaires (Python 3.9+) : pour une clé commune, la valeur de `b` gagne.

```python
a = {'key1': 'abc', 'key2': 'xyz'}
b = {'key2': 'nouveau', 'key3': 'def'}

print(a | b)     # {'key1': 'abc', 'key2': 'nouveau', 'key3': 'def'}
print(list(a))   # ['key1', 'key2'] : ordre d'insertion

for cle, valeur in a.items():
    print(cle, valeur)
```

<!-- .element: class="big-code" -->

Notes:
Le dictionnaire conserve l'ordre dans lequel les clés ont été ajoutées. Cet ordre est garanti par le langage depuis Python 3.7. Ce n'est donc plus un détail d'implémentation : on peut s'y fier.

`a | b` crée un nouveau dictionnaire, sans modifier `a` ni `b`. Pour fusionner sur place, on écrit `a |= b`.

Pour parcourir un dictionnaire, on itère sur `items()` avec deux variables : `for cle, valeur in a.items():`. C'est l'unpacking, vu dans la slide idiomes.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 03

**Opérations sur les listes**

```python
a = [10, 30, 20]

a[0]                 # 10
# a[3]                 # IndexError: list index out of range
a += [40]            # [10, 30, 20, 40] : équivalent à a.append(40)
a.extend([50, 60])   # [10, 30, 20, 40, 50, 60]
```

<!-- .element: class="big-code" -->

Notes:
`a += '40'` ne fait pas ce qu'on croit : une chaîne est un itérable de caractères, donc `+=` ajoute `'4'` puis `'0'`. Pour ajouter un élément, on passe une liste (`[40]`) ou on utilise `append()`. Pour en ajouter plusieurs, `extend()`.

`a[3]` est hors limites : la liste a 3 éléments, dont les index vont de 0 à 2. Ce n'est pas une valeur nulle, c'est une erreur, `IndexError`.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 03

**Inverser et trier une liste**

```python
a = [10, 30, 20]

a.reverse()                # modifie a sur place, ne renvoie rien
print(a)                   # [20, 30, 10]
print(list(reversed(a)))   # [10, 30, 20] : reversed() renvoie un itérateur
print(sorted(a))           # [10, 20, 30] : nouvelle liste, a ne change pas
print(a)                   # [20, 30, 10]
```

<!-- .element: class="big-code" -->

Notes:
`reverse()` est une méthode : elle modifie la liste et renvoie `None`. Écrire `a = a.reverse()` efface donc la liste.

`reversed(a)` renvoie un itérateur, pas une liste : il faut le consommer, avec `list(...)` ou une boucle `for`.

`sorted(a)` renvoie une nouvelle liste triée et laisse `a` intact. La méthode `a.sort()` trie la liste sur place.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 03

**Opération sur les sets**

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
```

<!-- .element: class="big-code" -->

![](./assets/images/set_operations.png 'center h-600')

Notes:
Un set est une collection non ordonnée, sans doublons. Avec A et B :

- `A | B` (union) : {1, 2, 3, 4, 5, 6, 7, 8}
- `A & B` (intersection) : {4, 5}
- `A - B` (différence) : {1, 2, 3}
- `A ^ B` (différence symétrique) : {1, 2, 3, 6, 7, 8}

Les méthodes équivalentes sont `union()`, `intersection()`, `difference()` et `symmetric_difference()`.
