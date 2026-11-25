"""Vérifications du lab step-02 : lancez ce fichier pour voir vos résultats.

uv run python steps/step-02/verifier.py
"""

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


def verifier_1():
    assert main.retirer("100", 30) == 70
    assert main.retirer("abc", 30) is None
    try:
        main.retirer("10", 50)
    except main.SoldeInsuffisantError as erreur:
        assert erreur.manque == 40
        assert str(erreur) == "Solde insuffisant : il manque 40"
    else:
        raise AssertionError("retirer('10', 50) doit lever SoldeInsuffisantError")


def verifier_2():
    with tempfile.TemporaryDirectory() as dossier:
        fichier = Path(dossier) / "input.txt"
        fichier.write_text("Hello\nWorld\n", encoding="utf-8")
        assert main.charger_mots(fichier) == {"Hello", "World"}
        assert main.charger_mots(Path(dossier) / "absent.txt") == set()


def verifier_3():
    with tempfile.TemporaryDirectory() as dossier:
        entree = Path(dossier) / "input.txt"
        sortie = Path(dossier) / "output.txt"
        entree.write_text("Hello\nWorld\n", encoding="utf-8")

        assert main.append_if_missing("Hello", entree, sortie) is False
        assert not sortie.exists()
        assert main.append_if_missing("Hell", entree, sortie) is True
        assert sortie.read_text(encoding="utf-8") == "Hell\n"
        assert main.append_if_missing("Hell", Path(dossier) / "absent.txt", sortie) is True
        assert sortie.read_text(encoding="utf-8") == "Hell\nHell\n"


def verifier_4():
    assert main.parser_ligne("Ada;36") == ("Ada", 36)
    assert main.parser_ligne(" Ada ; 36 ") == ("Ada", 36)
    for ligne in ("Ada", "Ada;36;x", ";36", "Ada;abc", ""):
        try:
            main.parser_ligne(ligne)
        except ValueError as erreur:
            assert str(erreur) == f"Ligne invalide : {ligne}", f"message inattendu : {erreur}"
        else:
            raise AssertionError(f"parser_ligne({ligne!r}) doit lever ValueError")


def verifier_5():
    with tempfile.TemporaryDirectory() as dossier:
        fichier = Path(dossier) / "personnes.txt"
        fichier.write_text("Ada;36\n\noups\nAlan;41\nBob;x\n", encoding="utf-8")
        assert main.lire_personnes(fichier) == ([("Ada", 36), ("Alan", 41)], ["oups", "Bob;x"])
        assert main.lire_personnes(Path(dossier) / "absent.txt") == ([], [])


def verifier_6():
    appels = []

    def capricieuse():
        appels.append(1)
        if len(appels) < 3:
            raise RuntimeError(f"échec {len(appels)}")
        return "ok"

    assert main.reessayer(capricieuse, 3) == "ok"
    assert len(appels) == 3

    appels.clear()
    try:
        main.reessayer(capricieuse, 2)
    except RuntimeError as erreur:
        assert str(erreur) == "échec 2", "il faut relever la dernière exception"
    else:
        raise AssertionError("reessayer doit relever l'exception si tous les essais échouent")
    assert len(appels) == 2

    appels.clear()
    appels.extend([1, 1])  # la fonction réussit dès le premier appel suivant
    assert main.reessayer(capricieuse, 5) == "ok"
    assert len(appels) == 3


if __name__ == "__main__":
    lancer([verifier_1, verifier_2, verifier_3], [verifier_4, verifier_5, verifier_6])
