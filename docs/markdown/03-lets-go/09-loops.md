<!-- .slide: class="with-code" -->

# Les bases - 08

**Les boucles : `for` et `while`**

* **for** parcourt tout itérable (liste, chaîne, dictionnaire) ou itérateur (générateur).
* On utilise souvent `range(stop)` ou `range(start, stop, pas)`.
* **while** répète tant que la condition est vraie.

```python
for i in range(3):          # 0, 1, 2
    print(i)

n = 3
while n > 0:
    print(n)                # 3, 2, 1
    n -= 1
```

<!-- .element: class="big-code" -->

Notes:
On itère sur tout ce qui est un itérable (une liste, une chaîne de caractères, un dictionnaire) ou un itérateur (un objet, un générateur).

`while` sert quand on ne sait pas à l'avance combien de tours on fera : on répète tant qu'une condition reste vraie. Il faut modifier la variable testée (ici `n -= 1`), sinon la boucle ne s'arrête jamais. Dans le doute, préférez `for`.

Attention aux habitudes des autres langages : Python n'a pas de `i++`. On écrit `i += 1`.
