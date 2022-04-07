<!-- .slide: -->

# Les bases - 05

**Les variables**

* A savoir : comme pour la déclaration, on peut assigner plusieurs variables sur une même ligne :

```python
x, y = 42, 3.14
x = y = 42
dictionary: dict[str, Any] = {"key": "value", "key_2": {}}
```

<!-- .element: class="big-code" -->
<br>

* Très pratique pour faire un swap :
```python
x, y = y, x
```
<!-- .element: class="big-code" -->
