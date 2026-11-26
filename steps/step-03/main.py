"""Lab step-03 : aller plus loin (10 minutes).

Complétez les trous (trois underscores) et ajoutez les décorateurs demandés, puis vérifiez avec :
    uv run python steps/step-03/verifier.py

Les exercices 4 à 6 (bonus) n'ont pas de trous : écrivez les fonctions à partir de la consigne.
"""

import functools
import os
from collections.abc import Callable, Generator, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from types import FunctionType
from typing import Any


# Exercice 1 : décorateur, *args et **kwargs, functools.wraps
def log_decorator(func: FunctionType) -> Callable[..., Any]:
    """Affiche "Appel de <nom de la fonction>" avant d'appeler func, puis renvoie son résultat."""

    # Conserver le nom et la docstring de func : ajouter le décorateur functools.wraps
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Appel de {___}")  # le nom de la fonction décorée
        return ___  # appeler func avec tous les arguments reçus

    return wrapper


# Appliquer le décorateur log_decorator à additionner
def additionner(a: int, b: int) -> int:
    """Additionne deux nombres."""
    return a + b


# Exercice 2 : lambda, sorted, compréhension de liste
def noms_adultes(people: list[dict[str, Any]]) -> list[str]:
    """Renvoie les noms des personnes majeures (18 ans ou plus), triées par âge croissant.

    Exemple : avec Alice (30 ans), Bob (12 ans) et Eve (21 ans), renvoie ["Eve", "Alice"].
    """
    # Trier people par âge : sorted avec une lambda comme clé
    tries = ___
    # Compréhension de liste : les noms des personnes d'au moins 18 ans
    return ___


# Exercice 3 : dataclass, property, __str__, classmethod
# Ajouter le décorateur qui génère __init__, __repr__ et __eq__
class Person:
    """Une personne avec un nom et un âge."""

    name: str
    age: int

    # Ajouter le décorateur qui transforme is_adult en propriété
    def is_adult(self) -> bool:
        """True si la personne a 18 ans ou plus."""
        return ___

    def __str__(self) -> str:
        # Renvoyer le texte "Alice (30 ans)"
        return ___

    # Ajouter le décorateur qui fait de from_dict une méthode de classe
    def from_dict(cls, data: dict[str, Any]) -> Person:
        """Construit une Person à partir d'un dict avec les clés "name" et "age"."""
        return ___


# Exercice 4 : générateur (yield)
def decouper(elements: list[Any], taille: int) -> Iterator[list[Any]]:
    """Découpe une liste en morceaux de `taille` éléments, en les produisant un à un (yield).

    Le dernier morceau peut être plus court.
    Exemple : list(decouper([1, 2, 3, 4, 5], 2)) renvoie [[1, 2], [3, 4], [5]].
    """
    raise NotImplementedError


# Exercice 5 : décorateur qui prend un argument (fabrique de décorateurs)
def repeter(fois: int) -> Callable[..., Any]:
    """Décorateur paramétré : @repeter(3) appelle la fonction décorée 3 fois de suite.

    - Le décorateur passe ses arguments à chaque appel et renvoie la liste des résultats.
    - Il conserve le nom et la docstring de la fonction (functools.wraps).
    - Exemple : si f() renvoie 1, puis 2, puis 3, f() décorée par @repeter(3) renvoie [1, 2, 3].
    """
    raise NotImplementedError


# Exercice 6 : gestionnaire de contexte
@contextmanager
def changer_dossier(chemin: Path) -> Generator[None]:
    """Se place dans `chemin` (os.chdir) le temps du bloc with, puis revient au dossier d'origine.

    Le retour au dossier d'origine doit avoir lieu même si le bloc with lève une exception.
    Exemple : with changer_dossier(Path("/tmp")): ... ; ici, on est revenu où on était.
    """
    raise NotImplementedError
