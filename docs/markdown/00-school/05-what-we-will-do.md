<!-- .slide: class="with-code center" -->

# Déroulement de la formation

<br>

Récupérer et préparer le repository :

```bash
git clone https://github.com/sfeir-open-source/sfeir-school-python.git
cd sfeir-school-python
uv sync
uv run python steps/step-00/check_env.py
```

<!-- .element: class="big-code" -->

Notes:
Cloner le dépôt, puis installer les dépendances une seule fois avec `uv sync`. uv crée l'environnement virtuel du projet et installe les bibliothèques figées dans `uv.lock`. Vous n'avez pas besoin d'activer le venv : toutes les commandes passent par `uv run`.

`check_env.py` affiche la version de Python (3.14 attendue) et vérifie que `fastapi`, `sqlmodel` et `fastmcp` s'importent correctement. Si cette commande passe, votre environnement est prêt pour toute la journée.

##==##

<!-- .slide: -->

# Programme de la journée

| Bloc | Contenu | Durée | Lab |
|---|---|---|---|
| 0 | Accueil | 10 min | step-00 : vérifier l'environnement |
| 1 | Pourquoi Python | 15 min | Aucun |
| 2 | Installation | 15 min | Fait au bloc 0 |
| 3 | Les bases | 75 min | step-01, step-02 |
| 4 | Aller plus loin | 90 min | step-03 |
| 5 | FastAPI | 80 min | fastapi step-01 et 02 |
| 6 | MCP | 75 min | mcp step-01 + bonus |
| 7 | Conclusion | 10 min | Aucun |

Notes:
Environ 6 h 30 de formation, pauses comprises : les blocs durent 370 minutes au total, ce qui laisse environ 20 minutes de pauses. Les blocs 3 à 6 sont les plus denses : ce sont eux qui occupent la majorité du temps pratique.

Le bloc 4 est allégé par rapport aux slides : on y voit les notions avancées (générateurs, décorateurs, classes, dataclass), et le lab step-03 ne pratique que les décorateurs, les lambdas, les compréhensions et une dataclass (avec property et classmethod). Les générateurs et les gestionnaires de contexte ne sont pratiqués que dans les exercices bonus.

Le bloc 5 (FastAPI) reprend tout ce qui a été vu le matin : décorateurs, classes Pydantic, context manager `lifespan`, coroutines.

##==##

<!-- .slide: -->

# Déroulement de la formation

**Comment fonctionne un lab ?**

* Chaque étape a deux dossiers :
  * `step-XX` : l'énoncé et les tests, à compléter
  * `step-XX-solution` : la solution, pour vous débloquer
* Lancer les tests de l'étape :

```bash
uv run pytest steps/step-XX
```

Notes:
Le pattern est le même pour toutes les étapes. D'abord les concepts en slides, puis le lab dans le dossier `step-XX`. Les tests échouent tant que l'exercice n'est pas terminé, puis passent une fois la fonction correcte.

Si vous êtes bloqué plus de quelques minutes, regardez le dossier `-solution` correspondant, puis reprenez l'exercice de zéro sans recopier : c'est en réécrivant que le concept s'installe.
