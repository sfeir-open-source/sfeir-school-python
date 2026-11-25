<!-- .slide: -->

# Les bases - 09

**Les exceptions**

* Une exception interrompt le déroulement normal du code.
* Si elle n'est pas gérée, elle arrête le programme et affiche une trace (traceback).
* C'est le mécanisme usuel pour gérer une erreur prévue : `try` / `except`.
* Toutes les exceptions héritent de `BaseException`.

##==##

<!-- .slide: -->

# Les bases - 09

**La hiérarchie des exceptions**

```text
BaseException
├── SystemExit          sys.exit()
├── KeyboardInterrupt   Ctrl+C
├── GeneratorExit       generator.close()
└── Exception           erreurs « classiques »
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   └── FileNotFoundError
    ├── TypeError
    ├── ValueError
    └── ...
```

En pratique, on capture `Exception`, jamais `BaseException` : sinon on intercepte aussi Ctrl+C et `sys.exit()`.

##==##

<!-- .slide: -->

# Les bases - 09

**Les exceptions courantes**

| Exception | Déclenchée quand… |
|---|---|
| `TypeError` | le type d'une opération est incorrect : `1 + "a"` |
| `ValueError` | le type est bon, la valeur non : `int("abc")` |
| `KeyError` | une clé est absente d'un dictionnaire : `d["x"]` |
| `IndexError` | un index est hors de la liste : `liste[10]` |
| `AttributeError` | l'attribut n'existe pas : `"a".uppper()` |
| `ZeroDivisionError` | une division par zéro : `1 / 0` |
| `FileNotFoundError` | le fichier n'existe pas (sous-classe de `OSError`) |
| `ImportError` | un import échoue (`ModuleNotFoundError` en est une sous-classe) |
| `StopIteration` | un itérateur est épuisé (`next()`) |
| `NotImplementedError` | méthode à implémenter dans une sous-classe |

Notes:
Cette liste couvre la plupart des erreurs rencontrées au quotidien. On reconnaît une exception à son nom, qui se termine par `Error` pour les erreurs, et souvent à son message.

`EnvironmentError` et `IOError` n'apparaissent plus dans la liste : ce sont des alias de `OSError` en Python 3. On écrit `OSError`, ou plus précisément `FileNotFoundError` si c'est le cas.

`NotImplementedError` hérite de `RuntimeError`. C'est l'exception à lever dans une méthode abstraite que les sous-classes doivent redéfinir.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 09

**Les exceptions : `try` / `except` / `else` / `finally`**

```python
def lire_age(texte: str) -> int | None:
    try:
        age = int(texte)
    except ValueError:
        print("Ce n'est pas un nombre")
        return None
    else:
        print("Conversion réussie")
        return age
    finally:
        print("Terminé")


lire_age("42")   # Conversion réussie, Terminé
lire_age("abc")  # Ce n'est pas un nombre, Terminé
```

<!-- .element: class="medium-code" -->

Notes:
- `try` : le code qui peut échouer, ici la conversion d'un texte en entier.
- `except` : la gestion de l'erreur. On cible une exception précise (`ValueError`), jamais un `except:` nu.
- `else` : exécuté seulement si aucune exception n'a été levée.
- `finally` : exécuté dans tous les cas, avec ou sans erreur, même si la fonction retourne avant. C'est l'endroit des libérations de ressources, même si `with` est plus idiomatique pour les fichiers.

Cas typique : lire une valeur saisie par l'utilisateur ou lue dans un fichier, qui peut ne pas être un nombre. `int("42")` réussit, donc on passe par `else` puis `finally`. `int("abc")` lève `ValueError`, donc on passe par `except` puis `finally`.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 09

**Les exceptions métier**

* Créer ses propres exceptions permet de capturer des erreurs métier précises.

```python
class SoldeInsuffisantError(Exception):
    """Levée quand le solde ne couvre pas le retrait."""
```

* Depuis Python 3.11, `add_note()` ajoute du contexte à une exception.

```python
try:
    raise TypeError("Oups")
except TypeError as e:
    e.add_note("Information contextuelle supplémentaire")
    raise
```

<!-- .element: class="big-code" -->

Notes:
Une exception métier hérite de `Exception`, et son nom se termine par `Error`. Elle permet ensuite à l'appelant d'écrire `except SoldeInsuffisantError:`, ce qui est bien plus clair qu'un `except ValueError` générique.

`add_note()` ajoute une ligne au message affiché dans la trace, sans changer l'exception. Le `raise` final relance l'exception d'origine, avec la note. Ce code se termine donc par une erreur : c'est voulu.
