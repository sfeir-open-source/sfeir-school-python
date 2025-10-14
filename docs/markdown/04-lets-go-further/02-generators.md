<!-- .slide: -->

# Pour aller plus loin - 02

**Le générateur**

* C’est le mot clé “yield” qui s’utilise à la place de “return”.
* “yield” ne stoppe pas l’exécution de la fonction.
* “yield” permet d’envoyer une valeur pour celui qui consomme.
* La fonction s’arrête une fois que tout a été consommé.
* A ce moment là une exception “StopIteration” est levée.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 02

**Le générateur**

* Un exemple simple de générateur :

```python
def simple_generator():
  yield 1
  yield 2
  yield 3
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

<!-- .slide: -->

# Pour aller plus loin - 02

**Le générateur**

* Les avantages :
  * Efficace en mémoire (lazy evaluation = retourne un élément à la fois).
  * Code plus simple et lisible pour les flux de données.
  * Permet de gérer des séquences infinies.
  
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

##==##

<!-- .slide: class="tc-multiple-columns" -->

##++##

## Efficacité: Itérateur...

```python
def find_errors_in_log(file_path):
    with open(file_path) as f:
        # Tente de charger 10Go en mémoire
        lines = f.readlines()
    for line in lines:
        if "ERROR" in line:
            print(line)

# -> Crash! (MemoryError)
```      
      
##++##

##++##

## ... vs Générateur

```python
def read_log_lines(file_path):
    with open(file_path) as f:
        for line in f:
            # Ne charge qu'une ligne à la fois
            yield line

for line in read_log_lines("huge.log"):
    if "ERROR" in line:
        print(line)

# -> Fonctionne parfaitement !
```

##++##

##==##

<!-- .slide: -->

# Pour aller plus loin - 02

**Le générateur**

* Les inconvénients :
  * Le résultat n’est disponible qu’une fois.
  * Impossible de connaître la taille totale.
  * Impossible d'indexer le générateur.

