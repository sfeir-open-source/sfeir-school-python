<!-- .slide: -->

# Pour aller plus loin - 10

**Les tests unitaires**

* `pytest` : le standard pour les tests unitaires en Python.
* Les tests sont de simples fonctions qui vérifient un comportement.
* Les fixtures permettent d'initialiser l'environnement de test.

```python
    # File: test_math.py
    import pytest

    # Fixture qui prépare des données pour le test
    @pytest.fixture
    def sample_numbers():
        return [10, 20, 30]

    # Fonction à tester
    def sum_numbers(numbers):
        return sum(numbers) ## if someone change this behavior, test_sum_numbers will fail !

    # Test qui utilise la fixture "sample_numbers"
    def test_sum_numbers(sample_numbers):
        assert sum_numbers(sample_numbers) == 60
```
