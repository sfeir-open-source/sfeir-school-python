<!-- .slide: class="with-code" -->

# Les bases - 10

**Les imports**

* Permet d’utiliser les fonctions d’un package ou d’un module.
* Imports absolus :

```python
import os  # os.getcwd()
from os import get_cwd  # getcwd()
from os import *  # getcwd()
```

<!-- .element: class="big-code" -->

* Imports relatifs :

```python
from . import mod1  # mod1.func1
from .mod1 import func1  # func1
```

<!-- .element: class="big-code" -->

Notes:
Imports relatifs déconseillés (code peu maintenable + ne passe pas le linter)
