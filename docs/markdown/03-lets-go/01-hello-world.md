# Les bases - 01

**Hello, world!**

Interpréteur Python :

* Façon la plus rapide de tester du code
* Lancement avec `python3` (sans paramètre) dans le terminal
* `quit()`, `help(print)`, `dir(int)`

Notes:
Python est un langage interprété : il dispose d'un moteur d'exécution accessible directement. Tapez `python3` dans votre terminal pour démarrer l'interpréteur interactif, appelé REPL (Read, Eval, Print, Loop). Il lit votre saisie, l'évalue, affiche le résultat, puis recommence.

La session garde en mémoire les variables, fonctions et types créés, jusqu'à sa fermeture.

Trois commandes à connaître :

- `quit()` pour quitter (Ctrl+D sous macOS et Linux, Ctrl+Z puis Entrée sous Windows)
- `help(objet)` affiche la documentation d'une fonction, d'un type ou d'une bibliothèque. Une bibliothèque tierce doit d'abord être importée.
- `dir(objet)` liste les attributs et méthodes d'un type (`dir(int)`) ou d'un module (`import unittest`, puis `dir(unittest)`).

##==##

<!-- .slide: class="with-code" -->

# Les bases - 01

**Hello, world!**

```pycon
$ python3
Python 3.14.10 (...)
>>> print('Hello world!')
Hello world!
>>> quit()
$
```

<!-- .element: class="big-code" -->

Notes:
Exemple très simple, mais très efficace. Pas de compilation à lancer, pas d'installation tierce.

La bannière affiche la version de l'interpréteur : c'est la première vérification à faire quand un exemple ne se comporte pas comme attendu. Ici, 3.14.

Les lignes commençant par `>>>` sont la saisie ; les lignes sans préfixe sont la réponse de l'interpréteur.

##==##

<!-- .slide: class="with-code" -->

# Les bases - 01

**Hello, world!**

Fichier `main.py` :

```python
#!/usr/bin/env python3
print('Hello world!')
```

<!-- .element: class="big-code" -->

```bash
python3 main.py
```

Sous macOS ou Linux, après `chmod +x main.py` :

```bash
./main.py
```

Notes:
On écrit les instructions dans un fichier, un script, qu'on confie à l'interpréteur avec `python3 main.py`.

La première ligne, le shebang, indique au système quel interpréteur utiliser sous macOS et Linux. `#!/usr/bin/env python3` cherche `python3` dans le PATH : c'est plus portable qu'un chemin figé comme `/bin/python3`. Pour trouver le chemin de votre interpréteur, utilisez `which python3`.

Sous Windows, le shebang est ignoré : on lance le script avec `python main.py`.
