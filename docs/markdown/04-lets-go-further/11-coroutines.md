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
- **Modèle asynchrone** : Standard en Python moderne, essentiel pour le web (FastAPI, Django Async).
- **Coroutine** : Une fonction `async def` qui peut être mise en pause et reprise.
- **`await`** : Met en pause la coroutine actuelle, permettant à d'autres tâches de s'exécuter.
- **vs Threads** : `asyncio` est mono-thread, évitant les problèmes du GIL (Global Interpreter Lock) pour la concurrence I/O.
- **Contrôle** : Le changement de contexte se fait uniquement sur `await`, ce qui rend le code plus prévisible et moins sujet aux race conditions.
- **Event Loop** : Le "chef d'orchestre" qui gère et exécute les tâches en attente.


##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 09

**Les coroutines - `async/await`**

```python
```python
import asyncio
import httpx # Bibliothèque HTTP moderne et compatible async

# `async def` crée une coroutine. Seul ce type de fonction peut utiliser `await`.
async def fetch_and_print(url):
  # `async with` gère un context manager asynchrone.
  async with httpx.AsyncClient() as client:
    # `await` suspend la fonction, attend le résultat de la requête et permet à d'autres tâches de s'exécuter pendant ce temps.
    response = await client.get(url)
    print(f"Status for {url}: {response.status_code}")

# `main` doit aussi être une coroutine pour pouvoir `await` d'autres coroutines.
async def main():
    # `asyncio.gather` lance plusieurs tâches en parallèle et attend leur achèvement.
    await asyncio.gather(
        fetch_and_print("https://python.org/"),
        fetch_and_print("https://www.sfeir.com/")
    )

# `asyncio.run()` est le point d'entrée qui démarre l'event loop et exécute la coroutine principale `main`.
asyncio.run(main())
```
