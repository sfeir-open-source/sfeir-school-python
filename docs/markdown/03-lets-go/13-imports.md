<!-- .slide: class="with-code" -->

# Les bases - 11

**Les imports**

* Un import rend disponibles les fonctions d'un module ou d'un package.
* Imports absolus, recommandés par PEP 8 :

```python
import os
from os import getcwd

print(os.getcwd())
print(getcwd())
```

<!-- .element: class="big-code" -->

* `from os import *` est à éviter : il importe des noms non explicités et pollue l'espace de noms.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 11

**Les imports relatifs**

* Dans un package, un import relatif explicite utilise le point `.` pour désigner le package courant.
* PEP 8 les accepte, mais les imports absolus restent préférables.

```python
from . import mod1        # mod1.func1()
from .mod1 import func1   # func1()
```

<!-- .element: class="big-code" -->

Notes:
Les imports absolus indiquent le chemin complet depuis la racine du projet : c'est lisible, et ça fonctionne partout. `import os` puis `os.getcwd()` garde visible d'où vient la fonction. `from os import getcwd` raccourcit l'appel, au prix d'un nom moins explicite.

`from os import *` importe tous les noms publics du module. On ne sait plus d'où vient une fonction, et deux modules peuvent se masquer mutuellement. On l'évite, y compris dans les exemples.

Les imports relatifs (`from . import mod1`) fonctionnent seulement à l'intérieur d'un package : lancés directement comme script, ils échouent. PEP 8 les accepte pour les imports explicites, mais ils sont moins pratiques à déplacer. Dans le doute, préférez l'absolu.
