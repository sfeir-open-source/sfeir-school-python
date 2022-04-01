<!-- .slide: class="with-code" -->

# Pour aller plus loin - 04

**Les lambdas**

* Une lambda est une fonction anonyme d’une seule ligne.

```python
get_xy = lambda s: (float(s.split(' ')[0]), float(s.split(' ')[1]))
```

<!-- .element: class="big-code" -->

<br>

```python
get_xy('12.345 -6.789')  # (12.345, -6.789)
```

<!-- .element: class="big-code" -->

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 04

**Les lambdas**

* Une lambda est une fonction anonyme d’une seule ligne.

```python
is_palindrome = lambda s: s == s[::-1]
```

<!-- .element: class="big-code" -->

<br>

```python
is_palindrome('mon nom')
# True
```

<!-- .element: class="big-code" -->
