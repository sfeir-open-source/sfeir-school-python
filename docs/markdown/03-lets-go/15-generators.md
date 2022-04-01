<!-- .slide: -->

# Pour aller plus loin - 14

**Le générateur**

* Une fonction qui permet de produire une valeur à la fois.
* C’est le mot clé “yield” qui s’utilise à la place de “return”.
* “yield” ne stoppe pas l’exécution de la fonction.
* “yield” permet d’envoyer une valeur pour celui qui consomme.
* La fonction s’arrête une fois que tout a été consommé.
* A ce moment là une exception “StopIteration” est levée.

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 14

**Le générateur**

* Un exemple simple de générateur :

```python
def simple_generator():
  yield 1
  yield 2
  yield 3
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: -->

# Pour aller plus loin - 14

**Le générateur**

* Les avantages :
  * Consomme moins de mémoire : un élément à chaque fois.
  * Le résultat peut dépendre de facteurs externes.
  * Lazy : uniquement ce qui est nécessaire est calculé.
  * Simple à écrire.

Notes:
The following are most important advantages of generators

Memory usage. Items can be processed one at a time, so there is generally no need to keep the entire list in memory.

The results can depend on outside factors, instead of having a static list.

Generators are lazy. This means that if you're using only the first five results of a generator, the rest won't even be calculated.

Generally, it is simpler to write than list generating functions.

##==##
<!-- .slide: -->

# Pour aller plus loin - 14

**Le générateur**

* Les inconvénients :
  * Le résultat n’est disponible qu’une fois.
  * Impossible de connaître la taille totale.
  * Impossible d'indexer le générateur.

Notes:
The following are most important disadvantages of generators

The results are available only once. After processing the results of a generator, it cannot be used again.

The size is unknown until you are done processing, which can be detrimental to certain algorithms.

Generators are not indexable, which means that simple_generator_function[2] will not work.

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 14

**Le générateur**

* Comment ça marche ?

```python
g = simple_generator()

next(g)  # 1
next(g)  # 2
next(g)  # 3
next(g)  # StopIteration
```

<!-- .element: class="big-code" -->

Notes:
The following are most important disadvantages of generators

The results are available only once. After processing the results of a generator, it cannot be used again.

The size is unknown until you are done processing, which can be detrimental to certain algorithms.

Generators are not indexable, which means that simple_generator_function[2] will not work.

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 14

**Le générateur**

* Le générateur retourne un itérable :

```python
for i in simple_generator():
  print i

list(simple_generator())
```

<!-- .element: class="big-code" -->

Notes:
Le mécanisme de “StopIteration” est automatique géré par la boucle

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Pour aller plus loin - 14

**La coroutine**

* C’est une fonction qui peut à la fois recevoir et produire de la donnée.

##--##

<br><br><br>

```python
def repeater():
  while True:
    received = yield
    print('Echo:', received)
```

##--##

<br><br><br>

```python
rp = repeater()

next(rp) # Start the coroutine
rp.send('Hello')  # Echo: Hello
rp.send('world!')  # Echo: world!
```
