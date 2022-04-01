<!-- .slide: class="with-code" -->

# Les bases - 06

**Les conditions**

* La déclaration if en Python s’écrit sans parenthèse :

```python
if condition:
  pass
```

<!-- .element: class="big-code" -->

<br>

* Comme pour les fonctions, la ligne se finit par le caractère “:”

Notes:
Parler des keywords “pass” / “del”

##==##
<!-- .slide: -->

# Les bases - 06

**Les conditions**

* La condition est une expression booléenne.
* Nous retrouvons les opérateurs classiques :

`==, <, <=, >, >=, &&, ||`

##==##
<!-- .slide: class="with-code" -->

# Les bases - 06

**Les conditions**

* La clause “**else**” s’utilise de façon classique et les “**elif**” peuvent être mis à la suite les uns des autres.


```python
if condition1:
  print('c1')
elif condition2:
  print('c2')
else:
  print('c3')
```

<!-- .element: class="big-code" -->

Notes:
Pas de switch => possibilité de faire une seule ligne en cas d’assignation ou autre.

##==##
<!-- .slide: -->
<!-- .slide: class="with-code" -->

# Les bases - 06

**Les conditions**

* Une ternaire est une condition sur une ligne.

```python
value = 42
is_positive = True if value >= 0 else False
```

<!-- .element: class="big-code" -->

# Les bases - 06

**Les conditions**

* Depuis python3.10, il est possible de faire un "switch-case" 
* Celaa fait une égalité strict entre `input_str` et la condition

```python
 match input_str:
    case "c1" | "c2":
        print("c1 or c2")
    case _:
        print("c3")

```


Notes:
Pas de switch => possibilité de faire une seule ligne en cas d’assignation ou autre.
