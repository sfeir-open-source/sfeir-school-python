"""Vérifie que l'environnement de l'atelier est prêt.

Lancer depuis la racine du projet :
    uv run python steps/step-00/check_env.py
"""

import importlib
import importlib.metadata
import sys

# Version minimale de Python attendue pour les ateliers.
PYTHON_MINIMUM = (3, 14)

# Bibliothèques à vérifier : (nom du module à importer, nom du paquet pour la version).
BIBLIOTHEQUES = [
    ("fastapi", "fastapi"),
    ("sqlmodel", "sqlmodel"),
    ("fastmcp", "fastmcp"),
    ("pytest", "pytest"),
]


def verifier_python() -> None:
    """Affiche la version de Python et avertit si elle est trop ancienne (sans bloquer)."""
    version = sys.version.split()[0]
    print(f"Python {version}")

    if sys.version_info < PYTHON_MINIMUM:
        minimum = ".".join(str(partie) for partie in PYTHON_MINIMUM)
        print(f"⚠️  Python {minimum} est recommandé, vous utilisez {version}.")
        print("   Depuis la racine du projet, lancez `uv sync` : uv installe la bonne version.")


def verifier_bibliotheque(module: str, paquet: str) -> bool:
    """Importe un module et affiche sa version. Renvoie True si tout se passe bien."""
    try:
        importlib.import_module(module)
        version = importlib.metadata.version(paquet)
    except (ImportError, importlib.metadata.PackageNotFoundError) as erreur:
        print(f"❌ {paquet} : import impossible ({erreur})")
        return False

    print(f"✅ {paquet} {version}")
    return True


def main() -> int:
    """Lance toutes les vérifications. Renvoie 0 si tout est prêt, 1 sinon."""
    verifier_python()
    print()

    # On vérifie toutes les bibliothèques, même si l'une d'elles échoue,
    # pour afficher le bilan complet d'un seul coup.
    resultats = [verifier_bibliotheque(module, paquet) for module, paquet in BIBLIOTHEQUES]

    print()
    if all(resultats):
        print("✅ Environnement prêt pour les ateliers.")
        return 0

    print("❌ Des bibliothèques manquent. Depuis la racine du projet, lancez `uv sync`.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
