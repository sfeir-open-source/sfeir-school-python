<!-- .slide: -->

# Les bases - 09

**Module vs Package**

| Module | Package |
| --- | --- |
| Un fichier `.py` | Un dossier de modules |
| `import my_module` | `from my_package import my_module` |

* Package : permet de structurer et d’organiser le projet en dossier.
* Un package doit contenir un `__init__.py` (bonne pratique).
* Possibilité d’exécuter le code d’un package :
  * doit contenir un fichier \_\_main\_\_.py
  * `$ python -m mon_package`
