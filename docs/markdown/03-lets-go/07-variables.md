<!-- .slide: class="with-code" -->

# Les bases - 06

**Les variables**

* Une variable n'a pas à être déclarée : elle existe à partir de sa première affectation.
* On peut affecter plusieurs variables sur une même ligne :

```python
x, y = 42, 3.14
x = y = 42
dictionary: dict[str, object] = {"key": "value", "key_2": {}}
```

<!-- .element: class="big-code" -->

<br>

* Très pratique pour faire un swap :

```python
x, y = 1, 2
x, y = y, x  # x vaut maintenant 2, y vaut 1
```

<!-- .element: class="big-code" -->

Notes:
L'annotation `dict[str, object]` se lit : un dictionnaire aux clés `str`, aux valeurs de n'importe quel type. `object` est la racine de tous les types. Si les valeurs ont un type plus précis, mieux vaut l'écrire, par exemple `dict[str, str | dict]`.

`Any` (module `typing`) existe aussi, mais il doit être importé : `from typing import Any`.

L'affectation `x, y = y, x` construit d'abord le tuple `(y, x)` à droite, puis le déballe à gauche. Pas besoin de variable temporaire.
