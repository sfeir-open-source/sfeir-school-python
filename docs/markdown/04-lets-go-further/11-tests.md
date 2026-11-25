<!-- .slide: -->

# Pour aller plus loin - 11

**Les tests unitaires**

* `pytest` : le standard pour les tests unitaires en Python.
* Les tests sont de simples fonctions qui vérifient un comportement.
* Les fixtures permettent d'initialiser l'environnement de test.
* `parametrize` permet de rejouer le même test avec plusieurs jeux de valeurs.

Notes:
Pas de `self.assertEqual` : un `assert` suffit. Quand il échoue, pytest affiche les valeurs comparées, ce qui rend le diagnostic rapide.
`uv run pytest` lance tous les tests du projet, selon la configuration de `pyproject.toml`. Pour un seul dossier : `uv run pytest steps/fastapi/step-01`.
Le fichier doit s'appeler `test_*.py` (ou `*_test.py`) pour être découvert automatiquement.

##==##

<!-- .slide: class="with-code" -->

# Pour aller plus loin - 11

**Les tests unitaires : exemple**

```python
# File: test_math.py
import pytest

# Fixture qui prépare des données pour le test
@pytest.fixture
def sample_numbers():
    return [10, 20, 30]

# Fonction à tester
def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)  # si quelqu'un change ce comportement, test_sum_numbers échouera !

# Test qui utilise la fixture "sample_numbers"
def test_sum_numbers(sample_numbers):
    assert sum_numbers(sample_numbers) == 60

# Même test avec plusieurs jeux de valeurs : un test par ligne
@pytest.mark.parametrize("numbers, expected", [([1, 2], 3), ([], 0), ([-1, 1], 0)])
def test_sum_numbers_parametrize(numbers, expected):
    assert sum_numbers(numbers) == expected
```

<!-- .element: class="medium-code" -->

Notes:
Une fixture est une fonction décorée par `@pytest.fixture`. pytest l'appelle pour chaque test qui demande son nom en paramètre.
`parametrize` produit un test par jeu de valeurs : ici trois tests à partir d'une seule fonction. En cas d'échec, pytest indique précisément le cas qui échoue.
N'oubliez pas `import pytest` : il sert aux fixtures comme aux marks.
Le code de cet exemple a été exécuté : les 4 tests passent.
