"""Lab step-02 : exceptions et fichiers (10 minutes).

Corrigé. Vérifiez avec :
    uv run python steps/step-02/verifier.py

Les exercices 4 à 6 (bonus) n'ont pas de trous : écrivez les fonctions à partir de la consigne.
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any


# Exercice 1 : exception métier avec attribut, try / except
class SoldeInsuffisantError(Exception):
    """Levée quand le solde ne couvre pas le retrait."""

    def __init__(self, solde: int, montant: int) -> None:
        # Mémoriser ce qui manque (montant - solde) dans self.manque
        self.manque = montant - solde
        # Appeler le constructeur parent avec le message "Solde insuffisant : il manque 40"
        super().__init__(f"Solde insuffisant : il manque {self.manque}")


def retirer(solde_texte: str, montant: int) -> int | None:
    """Renvoie le nouveau solde, ou None si solde_texte n'est pas un nombre.

    Lève SoldeInsuffisantError si le solde est inférieur au montant.
    """
    # Convertir solde_texte en entier ; si ce n'est pas un nombre, renvoyer None
    try:
        solde = int(solde_texte)
    except ValueError:
        return None
    # Lever SoldeInsuffisantError(solde, montant) si le solde est inférieur au montant
    if montant > solde:
        raise SoldeInsuffisantError(solde, montant)
    return solde - montant


# Exercice 2 : pathlib, exception FileNotFoundError, set
def charger_mots(chemin: Path) -> set[str]:
    """Renvoie l'ensemble des lignes du fichier, vide si le fichier n'existe pas."""
    try:
        contenu = Path(chemin).read_text(encoding="utf-8")  # lire le fichier avec pathlib
    except FileNotFoundError:
        return set()
    return set(contenu.splitlines())  # l'ensemble des lignes


# Exercice 3 : with, mode "a", réutilisation de l'exercice 2
def append_if_missing(word: str, input_path: Path, output_path: Path) -> bool:
    """Ajoute word (suivi d'un saut de ligne) à output_path s'il n'est pas une ligne de input_path.

    Renvoie True si le mot a été ajouté, False s'il était déjà présent.
    """
    if word in charger_mots(input_path):  # word est déjà dans les mots de input_path
        return False
    # Ajouter word en fin de output_path : ouvrir en mode "a" avec with, puis écrire
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(word + "\n")
    return True


# Exercice 4 : lever une exception avec son propre message
def parser_ligne(ligne: str) -> tuple[str, int]:
    """Parse une ligne "nom;age" et renvoie (nom, age).

    - Les espaces autour des champs sont ignorés : " Ada ; 36 " -> ("Ada", 36).
    - Lève ValueError("Ligne invalide : <ligne>") si la ligne n'a pas exactement deux champs, si le
      nom est vide ou si l'âge n'est pas un entier (le message cite la ligne telle qu'elle a été
      reçue, pas celui de int()).
    """
    champs = [champ.strip() for champ in ligne.split(";")]
    if len(champs) != 2 or not champs[0]:
        raise ValueError(f"Ligne invalide : {ligne}")
    try:
        return champs[0], int(champs[1])
    except ValueError:
        raise ValueError(f"Ligne invalide : {ligne}") from None


# Exercice 5 : réutiliser une fonction, fichier, tri valides / invalides
def lire_personnes(chemin: Path) -> tuple[list[tuple[str, int]], list[str]]:
    """Lit un fichier de lignes "nom;age" et renvoie (personnes valides, lignes invalides).

    - Utilisez parser_ligne. Les lignes vides sont ignorées.
    - Les lignes invalides sont renvoyées sans leur saut de ligne.
    - Un fichier absent donne ([], []).
    - Exemple : "Ada;36", "", "oups", "Alan;41" donnent ([("Ada", 36), ("Alan", 41)], ["oups"]).
    """
    valides: list[tuple[str, int]] = []
    invalides: list[str] = []
    try:
        lignes = chemin.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return valides, invalides
    for ligne in lignes:
        if not ligne.strip():
            continue
        try:
            valides.append(parser_ligne(ligne))
        except ValueError:
            invalides.append(ligne)
    return valides, invalides


# Exercice 6 : try / except / else, relever la dernière exception
def reessayer(fonction: Callable[[], Any], tentatives: int) -> Any:
    """Appelle fonction() jusqu'à `tentatives` fois et renvoie le résultat du premier appel réussi.

    - Si tous les appels lèvent une exception, la dernière est relevée.
    - fonction est appelée au plus `tentatives` fois, et pas une fois de plus dès qu'elle réussit.
    """
    for essai in range(1, tentatives + 1):
        try:
            return fonction()
        except Exception:
            if essai == tentatives:
                raise
