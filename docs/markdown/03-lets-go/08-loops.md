<!-- .slide: -->

# Les bases - 07

**Les boucles**

* Python permet de faire des boucles avec le mot clé **for**.
* Celui-ci permet d’itérer sur n’importe quel élément qui est soit :
  * Un itérable (une liste, une chaîne de caractère)
  * Un itérateur (une classe, un générateur)

##==##
<!-- .slide: class="with-code" -->

# Les bases - 07

**Les boucles**

* Par exemple, pour itérer de 0 à 9 avec un pas de 1 (par défaut) :

```python
def is_palindrome(s):
  for i in range(0, len(s)):
    if s[i] != s[len(s)-i-1]:
      return False
  return True
```

<!-- .element: class="big-code" -->

Notes:
Range renvoie une liste => itérable
range(start, stop not included, step)

##==##
<!-- .slide: class="with-code" -->

# Les bases - 07

**Les boucles**

* On peut également utiliser le mot clé **while** :

```python
def is_palindrome(s):
  copy = list(s)
  while len(copy) > 0:
    if s[len(s)-len(copy)] != copy.pop:
      break
  return True if len(copy) else False
```

<!-- .element: class="big-code" -->
