<!-- .slide: -->

# Les bases - 10

**Module vs Package**

| Module | Package |
| --- | --- |
| Un fichier `.py` | Un dossier de modules |
| `import my_module` | `from my_package import my_module` |

* Package : permet de structurer et d'organiser le projet en dossiers.
* Un package classique contient un fichier `__init__.py` (bonne pratique).
* Un package peut être exécuté directement :
  * il doit contenir un fichier `__main__.py` ;
  * `python -m mon_package`

Notes:
Un module est un fichier `.py`. Un package est un dossier de modules. Le fichier `__init__.py` marque le dossier comme package classique et peut contenir de l'initialisation. Depuis Python 3.3, un dossier sans `__init__.py` reste importable, comme « paquet d'espace de noms » (namespace package), mais on garde `__init__.py` par bonne pratique.

`python -m mon_package` exécute le fichier `__main__.py` du package, comme `if __name__ == "__main__":` pour un fichier unique.
