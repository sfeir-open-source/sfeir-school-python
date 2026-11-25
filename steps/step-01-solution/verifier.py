"""Vérifications du lab step-01 : lancez ce fichier pour voir vos résultats.

uv run python steps/step-01/verifier.py
"""

import sys
import traceback

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


def verifier_1():
    assert main.presenter("Ada", "36") == "Ada a 36 ans (Lille), adulte"
    assert main.presenter("Alan", "12", "Paris") == "Alan a 12 ans (Paris), mineur"
    assert main.presenter("Eve", "18") == "Eve a 18 ans (Lille), adulte"


def verifier_2():
    assert main.bilan([12, 8, 14]) == (14, 11.3, "admis")
    assert main.bilan([5, 9]) == (9, 7.0, "refusé")
    assert main.bilan([10]) == (10, 10.0, "admis")


def verifier_3():
    resultat = main.analyser("un deux un trois")
    assert resultat == ({"un": 2, "deux": 1, "trois": 1}, "un", ["deux", "trois", "un"], "trois")
    assert main.analyser("a b b")[1] == "b"


def verifier_4():
    assert main.formater_duree(3725) == "1h 02min 05s"
    assert main.formater_duree(3600) == "1h 00min 00s"
    assert main.formater_duree(125) == "2min 05s"
    assert main.formater_duree(60) == "1min 00s"
    assert main.formater_duree(59) == "59s"
    assert main.formater_duree(0) == "0s"


def verifier_5():
    assert main.est_palindrome("Esope reste ici et se repose") is True
    assert main.est_palindrome("A man, a plan, a canal: Panama") is True
    assert main.est_palindrome("Bonjour") is False
    assert main.est_palindrome("") is True


def verifier_6():
    resultat = main.regrouper_par_longueur(["un", "de", "un", "les", "a"])
    assert resultat == {1: ["a"], 2: ["un", "de"], 3: ["les"]}
    assert list(resultat) == [1, 2, 3]
    assert main.regrouper_par_longueur([]) == {}


if __name__ == "__main__":
    lancer([verifier_1, verifier_2, verifier_3], [verifier_4, verifier_5, verifier_6])
