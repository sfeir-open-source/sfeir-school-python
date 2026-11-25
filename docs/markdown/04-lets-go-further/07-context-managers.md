<!-- .slide: -->

# Pour aller plus loin - 07

**Les context managers**

* Gèrent une ressource : fichier, connexion, verrou
* S'utilisent avec le mot-clé `with`
* Automatisent l'initialisation et le nettoyage
* Garantissent le nettoyage, même en cas d'erreur (comme un `finally`)

Notes:
Le bloc `with` appelle `__enter__` à l'entrée, puis `__exit__` à la sortie, quoi qu'il arrive : fin normale, `return` ou exception.
C'est ce qui évite les fuites : un fichier resté ouvert, une connexion jamais fermée.
On a déjà utilisé `with` avec les générateurs (slide 02). Voici le mécanisme derrière.

##==##

<!-- .slide: class="with-code tc-multiple-columns col-offset-code" -->

##++##

# Pour aller plus loin - 07

**Un context manager en classe**

```python
class Chrono:
    def __enter__(self):
        print("Avant")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Après")
```

##++##

##++## class="with-code"

```python
with Chrono():
    print("Au milieu")

# Avant
# Au milieu
# Après
```

##++##

Notes:
`__enter__(self)` : sa valeur de retour est ce que reçoit le `as` (ici `self`).
`__exit__(self, exc_type, exc, tb)` reçoit les informations sur l'exception éventuelle. Ces trois arguments valent `None` s'il n'y a pas d'erreur.
Renvoyer une valeur vraie (`True`) dans `__exit__` supprime l'exception : c'est rare et à éviter. Sans `return`, ou avec `return False`, l'exception continue de remonter.

##==##

<!-- .slide: class="with-code tc-multiple-columns col-offset-code" -->

##++##

# Pour aller plus loin - 07

**Lire un fichier, sans puis avec `with`**

```python
path = "notes.txt"

f = open(path, encoding="utf-8")
try:
    for line in f:
        print(line, end="")
finally:
    f.close()
```

##++##

##++## class="with-code"

```python
path = "notes.txt"

with open(path, encoding="utf-8") as f:
    for line in f:
        print(line, end="")
```

##++##

Notes:
Sans `with`, il faut écrire le `try/finally` et penser au `close()`. Oublier le `finally`, c'est laisser le fichier ouvert en cas d'erreur.
Avec `with`, `open()` renvoie un context manager : `f` est fermé à la sortie du bloc, même si `print` lève une erreur.
`for line in f` lit ligne par ligne, sans charger tout le fichier (cf. générateurs). `readlines()` charge tout en mémoire.
`encoding="utf-8"` évite de dépendre de l'encodage par défaut de la machine, qui varie selon le système (Windows en particulier).
