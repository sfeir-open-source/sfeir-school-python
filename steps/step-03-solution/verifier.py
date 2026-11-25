"""Vérifications du lab step-03 : lancez ce fichier pour voir vos résultats.

uv run python steps/step-03/verifier.py
"""

import contextlib
import inspect
import io
import sys
import tempfile
import traceback
from pathlib import Path

import main

MARQUEUR = "_" * 3  # les trous à compléter


def executer(verification, libelle):
    """Exécute une vérification, affiche ✅ ou ❌ et renvoie True si elle réussit."""
    try:
        verification()
    except NotImplementedError:
        print(f"❌ {libelle} : à écrire (la consigne est dans main.py)")
    except Exception as erreur:
        if MARQUEUR in str(erreur):
            detail = "il reste des trous à compléter"
        elif isinstance(erreur, AssertionError):
            detail = traceback.extract_tb(erreur.__traceback__)[-1].line
        else:
            detail = f"{type(erreur).__name__} : {erreur}"
        print(f"❌ {libelle} : {detail}")
    else:
        print(f"✅ {libelle}")
        return True
    return False


def lancer(obligatoires, bonus):
    """Exécute toutes les vérifications (sans s'arrêter au premier échec) et affiche le bilan.

    Le code de sortie ne dépend que des exercices obligatoires : les bonus sont facultatifs.
    """
    reussis = sum([executer(v, f"exo {n}") for n, v in enumerate(obligatoires, start=1)])
    debut = len(obligatoires) + 1
    reussis_bonus = sum([executer(v, f"bonus {n}") for n, v in enumerate(bonus, start=debut)])
    print(
        f"\n{reussis}/{len(obligatoires)} exercices réussis, bonus : {reussis_bonus}/{len(bonus)}"
    )
    sys.exit(0 if reussis == len(obligatoires) else 1)


def capter(fonction, *args, **kwargs):
    """Appelle fonction et renvoie (résultat, texte affiché)."""
    sortie = io.StringIO()
    with contextlib.redirect_stdout(sortie):
        resultat = fonction(*args, **kwargs)
    return resultat, sortie.getvalue()


def verifier_1():
    assert capter(main.additionner, 2, 3) == (5, "Appel de additionner\n")
    assert main.additionner.__name__ == "additionner"
    assert main.additionner.__doc__ == "Additionne deux nombres."

    @main.log_decorator
    def multiplier(a, b=2):
        return a * b

    assert capter(multiplier, 3, b=4) == (12, "Appel de multiplier\n")


def verifier_2():
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 12},
        {"name": "Eve", "age": 21},
    ]
    assert main.noms_adultes(people) == ["Eve", "Alice"]
    assert main.noms_adultes([]) == []
    assert main.noms_adultes([{"name": "Bob", "age": 12}]) == []


def verifier_3():
    alice = main.Person("Alice", 30)
    assert alice == main.Person("Alice", 30)
    assert str(alice) == "Alice (30 ans)"
    assert alice.is_adult is True
    assert main.Person("Bob", 17).is_adult is False
    assert main.Person.from_dict({"name": "Alice", "age": 30}) == alice


def verifier_4():
    assert inspect.isgeneratorfunction(main.decouper), "decouper doit utiliser yield"
    assert list(main.decouper([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(main.decouper([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(main.decouper([], 3)) == []


def verifier_5():
    compteur = []

    @main.repeter(3)
    def tirer(offset=0):
        """Tire un numéro."""
        compteur.append(1)
        return len(compteur) + offset

    assert tirer() == [1, 2, 3]
    assert tirer(offset=10) == [14, 15, 16]
    assert tirer.__name__ == "tirer"
    assert tirer.__doc__ == "Tire un numéro."


def verifier_6():
    origine = Path.cwd()
    with tempfile.TemporaryDirectory() as dossier:
        cible = Path(dossier).resolve()
        with main.changer_dossier(cible):
            assert Path.cwd().resolve() == cible
        assert Path.cwd() == origine
        try:
            with main.changer_dossier(cible):
                raise RuntimeError("boom")
        except RuntimeError:
            pass
        assert Path.cwd() == origine, "il faut revenir au dossier d'origine même après une erreur"


if __name__ == "__main__":
    lancer([verifier_1, verifier_2, verifier_3], [verifier_4, verifier_5, verifier_6])
