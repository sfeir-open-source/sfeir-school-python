<!-- .slide: -->

# Pour aller plus loin - 09

**Les coroutines - `async/await`**

* Programmation asynchrone
  * Lancer plusieurs tâches en parallèle
  * Différer l'exécution d'une tâche
* Programmation coopérative 
  * Les tâches décident elles-mêmes de rendre la main (contrairement aux threads)
  * Changement de coroutine uniquement à un `await`

Notes:
Le modèle asynchrone a pris beaucoup d’ampleur dans les dernières versions de Python. La bibliothèque asyncio a été ajoutée en Python 3.4, ont suivi les mots-clés async et await en Python 3.5, et d’autres nouveautés dans les versions suivantes.

On entre dans une fonction en un point et on en sort en un autre point. On peut entrer, sortir et reprendre l'exécution d'une coroutine en plusieurs points.

La première raison est bassement technique : le GIL (Global Interpreter Lock) est une force de frottement dans l'interpréteur Python. Sa gestion picore sur le temps d'exécution des threads, de façon proportionnelle au nombre de tâches concurrentes en cours d'exécution. En somme, plus il y a de threads, plus le programme est ralenti, ce qui est embarrassant dans de nombreuses applications.

Où les interruptions sont prédictibles et explicites, donc tout le code entre deux interruptions est atomique : si vous ne placez pas d'interruption explicite entre deux lignes de code celles-ci seront exécutées d'un bloc, sans risque de modification extérieure.

Où l'ordonnancement entre les tâches n'est pas réalisé par le système d'exploitation, mais dans le userland et de façon plus intelligente et adaptée à la nature des tâches à exécuter en concurrence.

##==##
<!-- .slide: class="with-code" -->

# Pour aller plus loin - 09

**Les coroutines - `async/await`**

```python
import aiohttp
import asyncio

async def fetch_and_print(url):
  async with aiohttp.ClientSession() as session:
    response = await session.get(url)
    print(await response.text())

asyncio.run(fetch_and_print("https://python.org/"))
```

<!-- .element: class="big-code" -->

