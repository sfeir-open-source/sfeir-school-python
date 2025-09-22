

<!-- .slide: class="with-code" -->

# Les bases - 12

**Les Librairies standard**

## os

* Librarie permettant de manipuler les path, la lecture et l'ecriture de fichier: 


```python
from os import listdir, path

folder = "folder"
list_files: list[str] = listdir(folder) # List file and folder in specific path (here relative path)
for file_name in list_files: 
    file_path = path.join(folder, file_name) # Concat path of folder and file_name with "/"
    file = open(file_path, mode='r')
    # Reading the file line by line.
    line = file.readlines() # Read line one by one
    while line:
        print(line)
        line = file.readline()
    file.close() # Close file

```



##==##

<!-- .slide: class="with-code" -->
# Les bases - 12

**Les Librairies standard**

## re

* Librarie permettant de manipuler les regex:

```python
import re
str = "string"
regex_filter = r"^[a-z]" # Match la première lettre

match = re.search(regex_filter, str)
if match:
    print(match.group(0)) # return s
```
<!-- .element: class="big-code" -->


##==##

<!-- .slide: class="with-code" -->
# Les bases - 12

**Les Librairies standard**

## sys

* Librarie permettant de manipuler l'ecosystem python:

```python
# main.py
import sys

print(f"Args used {sys.argv[1]}, {sys.argv[2]}")
    
```
<!-- .element: class="big-code" -->

```bash
python3 main.py "test1" "test2" # Output Args used test1 test2
```
<!-- .element: class="big-code" -->


##==##

<!-- .slide: -->

# Les bases - 12

**Les Librairies standard**

Quelques modules incontournables de la bibliothèque standard :

|               |               |             |
|---------------|---------------|-------------|
| `asyncio`     | `collections` | `csv`       |
| `dataclasses` | `datetime`    | `enum`      |
| `json`        | `logging`     | `math`      |
| `pathlib`     | `random`      | `sqlite3`   |
| `subprocess`  | `threading`   | `typing`    |


Notes:
- **asyncio**: Programmation asynchrone, coroutines. Essentiel pour les I/O non bloquantes.
- **collections**: Types de données avancés (`Counter`, `defaultdict`, `deque`).
- **csv**: Lecture et écriture de fichiers CSV.
- **dataclasses**: Génération de classes de données sans code répétitif.
- **datetime**: Manipulation des dates et heures.
- **enum**: Création d'énumérations.
- **json**: Encodage et décodage du format JSON.
- **logging**: Journalisation des événements. Indispensable.
- **math**: Fonctions mathématiques.
- **pathlib**: Approche orientée objet pour manipuler les chemins du système de fichiers.
- **random**: Génération de nombres pseudo-aléatoires.
- **sqlite3**: Base de données légère, sans serveur.
- **subprocess**: Exécution de commandes externes.
- **threading**: Programmation concurrente avec des threads.
- **typing**: Support pour les indications de type. Crucial pour la robustesse du code.
