# Avant de se lancer

**Versions supportées**

| Version | Statut |
|---|---|
| 3.9 | Fin de vie depuis octobre 2025 |
| 3.10 | Fin de vie depuis le 1er octobre 2026 |
| 3.11 | Correctifs de sécurité jusqu'en octobre 2027 |
| 3.12 et 3.13 | Supportées |
| **3.14** | Supportée, utilisée dans cette formation (3.14.10) |
| 3.15 | Sortie le 9 octobre 2026 (3.15.2) |

* Recommandation : **Python 3.13 au minimum**.

Notes:
Vous verrez encore beaucoup de projets en Python 2. Il n'est plus maintenu depuis le 1er janvier 2020 : aucun correctif, y compris de sécurité. Pour un nouveau projet, on part de Python 3.

Une nouvelle version majeure sort chaque année, à l'automne : 3.14 en octobre 2025, 3.15 en octobre 2026. Une version n'est maintenue que pendant une période donnée. Le 1er octobre 2026, Python 3.10 est arrivé en fin de vie : il ne reçoit plus de correctifs. Pour un projet neuf, visez 3.13 ou plus récent.

Cette formation utilise Python 3.14, c'est la version figée dans `.python-version` et exigée par le `pyproject.toml` du dépôt.

##==##

<!-- .slide: -->

# Avant de se lancer

**Les spécificités du langage**

* Typage dynamique : les types sont vérifiés à l'exécution.
* Indentation pour la structure.
* Écosystème riche.
* Langage interprété : le code source est compilé en **bytecode** (fichiers `.pyc` dans `__pycache__`), puis exécuté par la machine virtuelle Python (détail à la slide suivante).

Notes:
* **Interprété** : Python ne produit pas de binaire natif que l'on lance à part. La compilation est automatique : chaque module est transformé en bytecode, puis la machine virtuelle exécute ce bytecode. La slide suivante détaille ce « faux-interprété ».

Attention à la nuance « ligne par ligne ». C'est une simplification : le module entier est d'abord compilé, ce qui signale les erreurs de syntaxe avant toute exécution. Ensuite, l'exécution suit l'ordre du code, instruction par instruction. Les fichiers `.pyc` sont des fichiers générés, dans `__pycache__` : on ne les versionne pas.

* **Typage** :
    * Dynamique : le type d'une valeur est vérifié à l'exécution, et une variable peut changer de type au cours du programme.
    * Graduel (optionnel) : on peut ajouter des annotations de type pour la clarté et l'analyse statique.
* **Indentation** : les blocs (fonctions, boucles, conditions) sont définis par l'indentation, pas par des accolades. La norme est de 4 espaces.
* **Écosystème** : une bibliothèque standard riche et des milliers de paquets sur PyPI, pour le web, la data, l'IA, etc.

##==##

<!-- .slide: -->

# Avant de se lancer

**Python est « faux-interprété »**

<svg viewBox="0 0 1100 490" width="100%" style="max-height:66vh" role="img" aria-label="Trois chaînes d'exécution : langage compilé, Python standard (bytecode puis machine virtuelle), Python avec JIT (le code chaud est compilé en code machine)" font-family="inherit"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#666"/></marker></defs><text x="10" y="84" font-size="21" text-anchor="start" fill="#222" font-weight="700">Langage compilé</text><text x="10" y="110" font-size="16" text-anchor="start" fill="#555" font-weight="400">C, Rust, Go : compilé avant</text><text x="10" y="214" font-size="21" text-anchor="start" fill="#222" font-weight="700">Python standard</text><text x="10" y="240" font-size="16" text-anchor="start" fill="#555" font-weight="400">compilé auto, puis interprété</text><text x="10" y="374" font-size="21" text-anchor="start" fill="#222" font-weight="700">Python + JIT</text><text x="10" y="400" font-size="16" text-anchor="start" fill="#555" font-weight="400">le code chaud est compilé</text><line x1="0" y1="150" x2="1200" y2="150" stroke="#ddd"/><line x1="0" y1="290" x2="1200" y2="290" stroke="#ddd"/><rect x="250" y="52" width="190" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="345.0" y="89.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Code source</text><rect x="480" y="52" width="190" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="575.0" y="89.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Code machine</text><rect x="940" y="52" width="150" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="1015.0" y="89.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">CPU</text><path d="M440,82 L476,82" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><path d="M670,82 L936,82" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><text x="805.0" y="70" font-size="15" text-anchor="middle" fill="#555" font-weight="400">exécuté directement</text><rect x="250" y="182" width="190" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="345.0" y="219.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Code source</text><rect x="480" y="182" width="190" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="575.0" y="208.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Bytecode</text><text x="575.0" y="230.0" font-size="15" text-anchor="middle" fill="#222">.pyc</text><rect x="710" y="182" width="190" height="60" rx="8" fill="#e6f0fb" stroke="#2a78d6" stroke-width="2"/><text x="805.0" y="208.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Machine virtuelle</text><text x="805.0" y="230.0" font-size="15" text-anchor="middle" fill="#222">interprète le bytecode</text><rect x="940" y="182" width="150" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="1015.0" y="219.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">CPU</text><path d="M440,212 L476,212" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><path d="M670,212 L706,212" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><path d="M900,212 L936,212" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><rect x="250" y="322" width="190" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="345.0" y="359.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Code source</text><rect x="480" y="322" width="190" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="575.0" y="348.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Bytecode</text><text x="575.0" y="370.0" font-size="15" text-anchor="middle" fill="#222">.pyc</text><rect x="710" y="322" width="190" height="60" rx="8" fill="#e6f0fb" stroke="#2a78d6" stroke-width="2"/><text x="805.0" y="348.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Machine virtuelle</text><text x="805.0" y="370.0" font-size="15" text-anchor="middle" fill="#222">code peu utilisé</text><rect x="940" y="322" width="150" height="60" rx="8" fill="#f3f4f7" stroke="#9aa0aa" stroke-width="2"/><text x="1015.0" y="359.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">CPU</text><path d="M440,352 L476,352" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><path d="M670,352 L706,352" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><path d="M900,352 L936,352" fill="none" stroke="#666" stroke-width="2.5" marker-end="url(#ah)"/><rect x="710" y="412" width="190" height="60" rx="8" fill="#fdebe3" stroke="#eb6834" stroke-width="2"/><text x="805.0" y="438.0" font-size="19" font-weight="700" text-anchor="middle" fill="#222">Code machine</text><text x="805.0" y="460.0" font-size="15" text-anchor="middle" fill="#222">JIT : code chaud</text><path d="M575.0,382 L575.0,442 L706,442" fill="none" stroke="#eb6834" stroke-width="2.5" marker-end="url(#ah)"/><path d="M900,442 L1015,442 L1015,386" fill="none" stroke="#eb6834" stroke-width="2.5" marker-end="url(#ah)"/></svg>

Notes:
Python n'est pas interprété « ligne par ligne » : il **compile déjà** le code source en bytecode (les fichiers `.pyc` dans `__pycache__`). Mais ce bytecode n'est pas du code machine : c'est une machine virtuelle (écrite en C) qui le lit et l'exécute instruction par instruction. C'est ce « faux-interprété » : une compilation vers un langage intermédiaire, puis une interprétation de celui-ci.

Un langage compilé (C, Rust, Go) produit directement du code machine avant l'exécution : le processeur l'exécute sans intermédiaire, d'où la vitesse.

Le JIT (« just-in-time », compilation à la volée) ne remplace pas ce schéma, il le complète. Pendant l'exécution, Python repère le code chaud, c'est-à-dire exécuté très souvent (le corps d'une boucle, une fonction appelée des millions de fois), et le compile en code machine, que le processeur exécute directement. Le reste continue de passer par la machine virtuelle. La différence avec « Python standard » : le bytecode `.pyc` est produit avant l'exécution et ne change pas, alors que le JIT fabrique du code machine pendant l'exécution, et seulement pour ce qui en vaut la peine.

Python 3.15 : le JIT est expérimental et désactivé par défaut (voir slide suivante). PyPy, vu dans le benchmark, est un autre interpréteur Python qui a un JIT bien plus abouti, d'où ses temps très bas.

##==##

<!-- .slide: class="with-code" -->

# Avant de se lancer

**Python 3.15 : `lazy import` et `frozendict`**

```python
lazy import json                       # PEP 810 : chargé au premier usage

config = frozendict({"debug": False})  # PEP 814 : dictionnaire immuable
config["debug"] = True                 # TypeError
```

<!-- .element: class="big-code" -->

* `lazy import` : démarrage plus rapide des grosses applications
* `frozendict` : une configuration partagée ne peut plus être modifiée par accident

Notes:
Ces exemples ne tournent que sous Python 3.15 : sous 3.14, `lazy` est une erreur de syntaxe et `frozendict` n'existe pas encore. Testés en local avec Python 3.15.0 : `json` n'apparaît dans `sys.modules` qu'après le premier `json.dumps`, et l'écriture dans le `frozendict` lève `TypeError: 'frozendict' object does not support item assignment`.

Imports paresseux (PEP 810) : le mot-clé `lazy` devant `import` retarde le chargement du module à sa première utilisation. Le mot-clé est « soft » : il reste un nom ordinaire ailleurs.

`frozendict` (PEP 814) : intégré, sans import. Cela rejoint la notion de données immuables vue avec les tuples.

##==##

<!-- .slide: class="with-code tc-multiple-columns jit-split" -->

##++##

# Avant de se lancer

**Python 3.15 : profileur par échantillonnage**

* Le profileur regarde où le programme passe son temps, sans le ralentir :

```bash
python -m profiling.sampling run main.py
```

<!-- .element: class="big-code" -->

##++##

##++##

![](./assets/images/profiling-screenshot.png 'center')

##++##

Notes:
JIT : Python 3.13 a introduit un compilateur « copy-and-patch » : au lieu de réinterpréter les mêmes instructions de bytecode à chaque tour de boucle, Python génère du code machine pour les morceaux exécutés souvent. Le gain dépend du programme : de quelques pourcents à une vingtaine (17 % sur fibo et 22 % sur bubble dans nos mesures de la slide suivante). Il est expérimental, donc désactivé par défaut. Il n'est disponible que si l'interpréteur a été compilé avec : c'est le cas du Python 3.15.2 installé par mise (testé : `sys._jit.is_available()` renvoie `True`, et `PYTHON_JIT=1` fait passer `is_enabled()` à `True`), mais pas de tous les paquets : le Python 3.15.0 Homebrew testé n'a pas le JIT. Vérifier avec `python -c "import sys; print(sys._jit.is_available())"`. Mesure rapide sur `fibo(32)` : environ 0,20 s sans JIT, 0,15 s avec.

Profileur : le paquet `profiling` (PEP 799) regroupe `profiling.sampling` (échantillonnage, surnommé Tachyon : il interroge le programme des milliers de fois par seconde, impact très faible) et `profiling.tracing` (déterministe, l'ancien `cProfile`, qui compte chaque appel). La capture à droite est une vraie sortie de `profiling.sampling run main.py` sur un script qui appelle `fibo` et un tri à bulles : on lit tout de suite que `fibo` et `bubble` concentrent l'essentiel des échantillons (colonne `sample%`).

Pour un flame graph HTML interactif : `python -m profiling.sampling run --flamegraph -o profil.html main.py`. Sur macOS, `profiling.sampling` demande des droits élevés (`sudo -E`), car il lit la mémoire du processus : à tester avant une démo. Les options : `python -m profiling.sampling run --help`.

##==##

<!-- .slide: -->
# Avant de se lancer

**Performances** : fibo(40) récursif, en secondes (plus court = plus rapide)

<svg viewBox="0 0 1200 504" width="100%" style="max-height:72vh" role="img" aria-label="Temps d'exécution de fibo(40) selon la version de Python et d'autres interpréteurs, en secondes, plus court = plus rapide" font-family="inherit"><rect x="170" y="14" width="16" height="16" rx="3" fill="#2a78d6"/><text x="194" y="28" font-size="18" fill="#333">CPython standard</text><rect x="400" y="14" width="16" height="16" rx="3" fill="#eb6834"/><text x="424" y="28" font-size="18" fill="#333">3.15 + JIT (expérimental)</text><rect x="720" y="14" width="16" height="16" rx="3" fill="#8a8f98"/><text x="744" y="28" font-size="18" fill="#333">Autres interpréteurs et langages</text><rect x="170" y="42" width="16" height="16" rx="3" fill="#1baf7a"/><text x="194" y="56" font-size="18" fill="#333">3.15 free-threaded (sans verrou global (GIL))</text><text x="170" y="92" font-size="20" font-weight="700" fill="#222">1 thread (fibo 1T)</text><line x1="170" y1="98" x2="170" y2="498" stroke="#bbb" stroke-width="1"/><text x="158" y="126" font-size="18" text-anchor="end" fill="#333">3.10</text><rect x="170" y="108" width="398.5" height="24" rx="4" fill="#2a78d6"><title>3.10 : 15,94 s</title></rect><text x="576.5" y="126" font-size="17" fill="#555">15,94 s</text><text x="158" y="162" font-size="18" text-anchor="end" fill="#333">3.11</text><rect x="170" y="144" width="235.2" height="24" rx="4" fill="#2a78d6"><title>3.11 : 9,41 s</title></rect><text x="413.2" y="162" font-size="17" fill="#555">9,41 s</text><text x="158" y="198" font-size="18" text-anchor="end" fill="#333">3.12</text><rect x="170" y="180" width="221.2" height="24" rx="4" fill="#2a78d6"><title>3.12 : 8,85 s</title></rect><text x="399.2" y="198" font-size="17" fill="#555">8,85 s</text><text x="158" y="234" font-size="18" text-anchor="end" fill="#333">3.13</text><rect x="170" y="216" width="220.5" height="24" rx="4" fill="#2a78d6"><title>3.13 : 8,82 s</title></rect><text x="398.5" y="234" font-size="17" fill="#555">8,82 s</text><text x="158" y="270" font-size="18" text-anchor="end" fill="#333">3.14</text><rect x="170" y="252" width="179.2" height="24" rx="4" fill="#2a78d6"><title>3.14 : 7,17 s</title></rect><text x="357.2" y="270" font-size="17" fill="#555">7,17 s</text><text x="158" y="306" font-size="18" text-anchor="end" fill="#333">3.15</text><rect x="170" y="288" width="173.5" height="24" rx="4" fill="#2a78d6"><title>3.15 : 6,94 s</title></rect><text x="351.5" y="306" font-size="17" fill="#555">6,94 s</text><text x="158" y="342" font-size="18" text-anchor="end" fill="#333">3.15 JIT</text><rect x="170" y="324" width="144.0" height="24" rx="4" fill="#eb6834"><title>3.15 JIT : 5,76 s</title></rect><text x="322.0" y="342" font-size="17" fill="#555">5,76 s</text><text x="158" y="378" font-size="18" text-anchor="end" fill="#333">3.15 free-threaded</text><rect x="170" y="360" width="175.8" height="24" rx="4" fill="#1baf7a"><title>3.15 free-threaded : 7,03 s</title></rect><text x="353.8" y="378" font-size="17" fill="#555">7,03 s</text><text x="158" y="414" font-size="18" text-anchor="end" fill="#333">PyPy 3.12</text><rect x="170" y="396" width="31.2" height="24" rx="4" fill="#8a8f98"><title>PyPy 3.12 : 1,25 s</title></rect><text x="209.2" y="414" font-size="17" fill="#555">1,25 s</text><text x="158" y="450" font-size="18" text-anchor="end" fill="#333">Node 26</text><rect x="170" y="432" width="34.8" height="24" rx="4" fill="#8a8f98"><title>Node 26 : 1,39 s</title></rect><text x="212.8" y="450" font-size="17" fill="#555">1,39 s</text><text x="158" y="486" font-size="18" text-anchor="end" fill="#333">Rust 1.97</text><rect x="170" y="468" width="2.2" height="24" rx="4" fill="#8a8f98"><title>Rust 1.97 : 0,09 s</title></rect><text x="180.2" y="486" font-size="17" fill="#555">0,09 s</text><text x="770" y="92" font-size="20" font-weight="700" fill="#222">4 threads (fibo 4T)</text><line x1="770" y1="98" x2="770" y2="498" stroke="#bbb" stroke-width="1"/><text x="758" y="126" font-size="18" text-anchor="end" fill="#333">3.10</text><rect x="770" y="108" width="384.5" height="24" rx="4" fill="#2a78d6"><title>3.10 : 67,29 s</title></rect><text x="1162.5" y="126" font-size="17" fill="#555">67,29 s</text><text x="758" y="162" font-size="18" text-anchor="end" fill="#333">3.11</text><rect x="770" y="144" width="284.2" height="24" rx="4" fill="#2a78d6"><title>3.11 : 49,73 s</title></rect><text x="1062.2" y="162" font-size="17" fill="#555">49,73 s</text><text x="758" y="198" font-size="18" text-anchor="end" fill="#333">3.12</text><rect x="770" y="180" width="221.3" height="24" rx="4" fill="#2a78d6"><title>3.12 : 38,73 s</title></rect><text x="999.3" y="198" font-size="17" fill="#555">38,73 s</text><text x="758" y="234" font-size="18" text-anchor="end" fill="#333">3.13</text><rect x="770" y="216" width="222.5" height="24" rx="4" fill="#2a78d6"><title>3.13 : 38,94 s</title></rect><text x="1000.5" y="234" font-size="17" fill="#555">38,94 s</text><text x="758" y="270" font-size="18" text-anchor="end" fill="#333">3.14</text><rect x="770" y="252" width="181.9" height="24" rx="4" fill="#2a78d6"><title>3.14 : 31,84 s</title></rect><text x="959.9" y="270" font-size="17" fill="#555">31,84 s</text><text x="758" y="306" font-size="18" text-anchor="end" fill="#333">3.15</text><rect x="770" y="288" width="185.9" height="24" rx="4" fill="#2a78d6"><title>3.15 : 32,54 s</title></rect><text x="963.9" y="306" font-size="17" fill="#555">32,54 s</text><text x="758" y="342" font-size="18" text-anchor="end" fill="#333">3.15 JIT</text><rect x="770" y="324" width="155.2" height="24" rx="4" fill="#eb6834"><title>3.15 JIT : 27,16 s</title></rect><text x="933.2" y="342" font-size="17" fill="#555">27,16 s</text><text x="758" y="378" font-size="18" text-anchor="end" fill="#333">3.15 free-threaded</text><rect x="770" y="360" width="41.4" height="24" rx="4" fill="#1baf7a"><title>3.15 free-threaded : 7,24 s</title></rect><text x="819.4" y="378" font-size="17" fill="#555">7,24 s</text><text x="758" y="414" font-size="18" text-anchor="end" fill="#333">PyPy 3.12</text><rect x="770" y="396" width="32.2" height="24" rx="4" fill="#8a8f98"><title>PyPy 3.12 : 5,64 s</title></rect><text x="810.2" y="414" font-size="17" fill="#555">5,64 s</text><text x="758" y="450" font-size="18" text-anchor="end" fill="#333">Node 26</text><text x="778" y="450" font-size="16" fill="#888" font-style="italic">non mesuré</text><text x="758" y="486" font-size="18" text-anchor="end" fill="#333">Rust 1.97</text><text x="778" y="486" font-size="16" fill="#888" font-style="italic">non mesuré</text></svg>

<p style="font-size:0.5em;margin:0">Source : <a href="https://blog.miguelgrinberg.com/post/how-fast-is-python-3-15">M. Grinberg, « How fast is Python 3.15? »</a>, oct. 2026 (Linux, Intel i5, 3.15.0rc3)</p>

Notes:
Source : Miguel Grinberg, « How fast is Python 3.15? » (05/10/2026), https://blog.miguelgrinberg.com/post/how-fast-is-python-3-15 — scripts : https://github.com/miguelgrinberg/pyspeed (`bash run.sh`). Mesuré sous Linux (Intel Core i5) avec 3.15.0rc3 ; toutes les versions ont été mesurées dans la même série, la comparaison est donc cohérente. 4T = quatre copies du calcul lancées en parallèle dans 4 threads (temps réel).

Lecture :
- De 3.10 à 3.11, le grand saut (projet Faster CPython) : environ 1,7x.
- 3.15 standard n'apporte qu'un gain mineur par rapport à 3.14.
- Le JIT (expérimental, `PYTHON_JIT=1`) gagne 17 à 22 %.
- Le build free-threaded (`python3.15t`) ne change rien en 1 thread, mais en 4 threads il est environ 4,5x plus rapide : sans GIL, les threads tournent vraiment en parallèle. Free-threading officiellement supporté depuis 3.14 (PEP 779), mais optionnel : c'est un interpréteur séparé.
- PyPy, Node et Rust (barres grises) situent les ordres de grandeur ; ce ne sont pas des versions de CPython. Node et Rust n'ont pas de mesure en 4 threads.

Tableau complet (secondes) — fibo 1T / bubble 1T / fibo 4T / bubble 4T :
3.10 : 15,94 / 3,99 / 67,29 / 16,60
3.11 : 9,41 / 2,62 / 49,73 / 10,75
3.12 : 8,85 / 2,73 / 38,73 / 10,98
3.13 : 8,82 / 2,83 / 38,94 / 11,13
3.14 : 7,17 / 2,06 / 31,84 / 8,72
3.15 (rc3) : 6,94 / 1,97 / 32,54 / 8,45
3.15 JIT : 5,76 / 1,54 / 27,16 / 6,64
3.15 free-threaded : 7,03 / 2,68 / 7,24 / 4,85
PyPy 3.12 : 1,25 / 0,11 / 5,64 / 0,52
Node 26.3 : 1,39 / 0,06 / – / –
Rust 1.97 : 0,09 / 0,04 / – / –
