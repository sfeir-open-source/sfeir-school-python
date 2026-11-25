"""Lab step-01 : les bases du langage (10 minutes).

Corrigé. Vérifiez avec :
    uv run python steps/step-01/verifier.py

Les exercices 4 à 6 (bonus) n'ont pas de trous : écrivez les fonctions à partir de la consigne.
"""


# Exercice 1 : types, f-string, ternaire, argument par défaut
def presenter(prenom: str, age_texte: str, ville: str = "Lille") -> str:
    """Renvoie "Ada a 36 ans (Lille), adulte" ; "mineur" si l'âge est inférieur à 18."""
    # Convertir age_texte en entier
    age = int(age_texte)
    # Choisir le statut avec une expression conditionnelle (ternaire)
    statut = "adulte" if age >= 18 else "mineur"
    return f"{prenom} a {age} ans ({ville}), {statut}"


# Exercice 2 : boucle for, calculs, ternaire, retour de plusieurs valeurs
def bilan(notes: list[int]) -> tuple[int, float, str]:
    """Renvoie (meilleure_note, moyenne, mention) ; la moyenne est arrondie à 1 décimale.

    La mention est "admis" si la moyenne est au moins 10, sinon "refusé".
    Exemple : bilan([12, 8, 14]) renvoie (14, 11.3, "admis").
    """
    total = 0
    # Additionner toutes les notes dans total (boucle for)
    for note in notes:
        total += note
    moyenne = round(total / len(notes), 1)
    mention = "admis" if moyenne >= 10 else "refusé"
    return max(notes), moyenne, mention


# Exercice 3 : dict, set, tri, unpacking
def analyser(texte: str) -> tuple[dict[str, int], str, list[str], str]:
    """Renvoie (occurrences par mot, mot le plus fréquent, mots distincts triés, dernier mot).

    Exemple : analyser("un deux un trois") renvoie
    ({"un": 2, "deux": 1, "trois": 1}, "un", ["deux", "trois", "un"], "trois").
    """
    mots = texte.split()
    compte: dict[str, int] = {}
    # Compter les occurrences de chaque mot (boucle for et dict)
    for mot in mots:
        compte[mot] = compte.get(mot, 0) + 1
    plus_frequent = max(compte, key=lambda mot: compte[mot])
    distincts = sorted(set(mots))
    # Déballer la liste : *debut récupère tous les mots sauf le dernier
    *debut, dernier = mots
    return compte, plus_frequent, distincts, dernier


# Exercice 4 : divmod, f-string avec format, logique conditionnelle
def formater_duree(secondes: int) -> str:
    """Convertit une durée en secondes en texte, du type "1h 02min 05s".

    - La première unité non nulle ouvre le texte, sans zéro devant ; les suivantes sont toujours
      affichées, sur 2 chiffres.
    - Exemples : 3725 -> "1h 02min 05s", 3600 -> "1h 00min 00s", 125 -> "2min 05s",
      60 -> "1min 00s", 59 -> "59s", 0 -> "0s".
    """
    minutes, sec = divmod(secondes, 60)
    heures, minutes = divmod(minutes, 60)
    if heures:
        return f"{heures}h {minutes:02d}min {sec:02d}s"
    if minutes:
        return f"{minutes}min {sec:02d}s"
    return f"{sec}s"


# Exercice 5 : méthodes de str, compréhension, slicing
def est_palindrome(texte: str) -> bool:
    """Dit si le texte se lit pareil dans les deux sens, sans tenir compte de la casse,
    des espaces ni de la ponctuation.

    Exemples : "Esope reste ici et se repose" -> True, "A man, a plan, a canal: Panama" -> True,
    "Bonjour" -> False. Une chaîne vide est un palindrome.
    """
    lettres = [c.lower() for c in texte if c.isalnum()]
    return lettres == lettres[::-1]


# Exercice 6 : dict de listes, ordre, doublons
def regrouper_par_longueur(mots: list[str]) -> dict[int, list[str]]:
    """Regroupe les mots par longueur.

    - Dans chaque liste, les mots gardent leur ordre d'apparition, sans doublon.
    - Les clés du dict sont dans l'ordre croissant.
    - Exemple : ["un", "de", "un", "les", "a"] -> {1: ["a"], 2: ["un", "de"], 3: ["les"]}.
    """
    groupes: dict[int, list[str]] = {}
    for mot in mots:
        liste = groupes.setdefault(len(mot), [])
        if mot not in liste:
            liste.append(mot)
    return dict(sorted(groupes.items()))
