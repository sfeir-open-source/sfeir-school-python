<!-- .slide: class="with-code" -->

# Les bases - 12

**Les librairies standard**

## pathlib: Manipuler les chemins et lire les fichiers, de façon orientée objet.

```python
from pathlib import Path

chemin = Path("donnees") / "notes.txt"

with open(chemin, encoding="utf-8") as f:
    for line in f:  # lecture ligne par ligne
        print(line.rstrip("\n"))

contenu = chemin.read_text(encoding="utf-8")  # tout le fichier d'un coup
```

<!-- .element: class="big-code" -->

Notes:
`pathlib` remplace `os.path` pour la plupart des usages. L'opérateur `/` assemble les chemins, quel que soit le système d'exploitation.

`with` ouvre le fichier et le referme automatiquement à la sortie du bloc, même en cas d'erreur. Sans `with`, il faut penser à appeler `close()`.

`for line in f` lit le fichier une ligne à la fois, sans charger tout le contenu en mémoire. `line.rstrip("\n")` retire le saut de ligne final. `read_text()` est plus court quand le fichier est petit.

Précisez toujours `encoding="utf-8"` : sans cela, l'encodage dépend du système.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 12

**Les librairies standard**

## re : Manipuler les expressions régulières.

```python
import re

texte = "string"
motif = r"^[a-z]"  # la première lettre, si elle est en minuscule

correspondance = re.search(motif, texte)
if correspondance:
    print(correspondance.group(0))  # s
```

<!-- .element: class="big-code" -->

Notes:
Le préfixe `r` désigne une chaîne brute : les antislashs ne sont pas interprétés par Python, ils sont lus par le moteur d'expressions régulières. C'est l'usage standard pour les motifs.

`re.search` renvoie un objet `Match` si le motif est trouvé, sinon `None` : on teste donc avec `if`. `group(0)` renvoie le texte trouvé.

Ne donnez pas le nom `str` à une variable : cela masque le type `str` intégré, et les erreurs qui en découlent sont difficiles à lire.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 12

**Les librairies standard**

## sys : Accéder à l'environnement du programme, notamment les arguments de la CLI.

```python
import sys

if len(sys.argv) < 3:
    sys.exit("Usage: python main.py <arg1> <arg2>")

print(f"Arguments : {sys.argv[1]}, {sys.argv[2]}")
```

<!-- .element: class="big-code" -->

```bash
python3 main.py "test1" "test2"   # Arguments : test1, test2
```

<!-- .element: class="big-code" -->

Notes:
`sys.argv` est une liste : `sys.argv[0]` est le nom du script, les arguments suivent. Sans la garde `if len(sys.argv) < 3`, lancer le script sans argument provoquerait une `IndexError`.

`sys.exit("message")` affiche le message sur la sortie d'erreur et termine le programme avec un code non nul. C'est le bon moyen de signaler un mauvais usage.

##==##

<!-- .slide: -->

# Les bases - 12

**Les librairies standard**

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
