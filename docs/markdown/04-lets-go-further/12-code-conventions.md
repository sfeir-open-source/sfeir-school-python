<!-- .slide: -->

# Bonnes pratiques - 15

**Les bonnes pratiques - convention de nommage**

* Python utilise des PEP (Python Enhancement Proposal) :
  * Proposer des évolutions au langage
  * Partager les bonnes pratiques
* PEP 8 - Style Guide for Python Code :
  * https://www.python.org/dev/peps/pep-0008/
* PEP 20 - The Zen of Python :
  * https://www.python.org/dev/peps/pep-0020/

##==##
<!-- .slide: -->

# Bonnes pratiques - 15

**Les bonnes pratiques - disposition du code**

* Le code doit être indenté en-dessous des parenthèses si la ligne est trop grande.
* Il faut de préférence indenter avec 4 espaces.
* Il ne faut pas dépasser 79 caractères par ligne (utiliser un “\”).
* Les opérateurs doivent être au début de la ligne si celle-ci est trop grande.
* Il faut utiliser 2 sauts de ligne pour séparer une classe.
* Il faut utiliser des caractères ASCII ou UTF-8.

##==##
<!-- .slide: -->

# Bonnes pratiques - 15

**Les bonnes pratiques - disposition du code**

* Un seul import par ligne.
* Les imports doivent être groupés dans l’ordre suivant :
  * imports des librairies standards
  * imports des librairies tierces
  * imports
* Préférer les imports absolus aux relatifs.
* Éviter d’importer un module en entier avec *

##==##
<!-- .slide: -->

# Bonnes pratiques - 15

**Les bonnes pratiques - disposition du code**

* Il est possible d’utiliser des ‘ ou “ pour les strings, mais garder la même convention.
* Pas d’espace avant ou après les parenthèses.
* Après une virgule toujours un espace.
* Pas plus d’un espace pour les assignations.
* Pas d’espace inutile à la fin des lignes.

##==##
<!-- .slide: class="with-code" -->

# Bonnes pratiques - 15

**Les bonnes pratiques - documentation**

* Un bloc de commentaire doit se faire avec des # :

```python
# First line
# Second line
```

<!-- .element: class="big-code" -->

* Un commentaire de ligne doit être précédé de 2 espaces :

```python
x = x + 1  # Compensate for border
```

<!-- .element: class="big-code" -->

* Tout module, fonction ou classe doit avoir une docstring :

```python
def function():
  """My function"""
  pass
```

<!-- .element: class="big-code" -->

Notes:
Docstring : permet de documenter la fonctionnalité macro de la fonction (paramètre, retour).

Commentaire (bloc ou ligne) : utile pour les détails d’implémentation.

##==##
<!-- .slide: -->

# Bonnes pratiques - 15

**Les bonnes pratiques - conventions de nommage**

* Variable : ne pas utiliser “l”, “O”, ou “I” comme unique caractère.
* Package et module : nom court, en minuscule, avec des _
* Classe : utiliser des majuscules pour séparer les mots.
* Exception : même convention, ajouter “Error” à la fin si nécessaire.
* Fonction et variable : en minuscule, mots séparés par des _
* Méthodes d’instance et de classe :
  * utiliser self / cls comme premier argument
  * si conflit avec un mot clé natif, ajouter un _ ou utiliser un synonyme
* Constante : en majuscule

##==##
<!-- .slide: -->

# Bonnes pratiques - 15

**Les bonnes pratiques - programmation**

* Comparaison avec None : utiliser “is” ou “is not”.
* Comparaison avec une classe : implémenter toujours l’ensemble des opérateurs.
* Function vs lambda : préférer des fonctions nommées, plus facile pour les erreurs.
* try/catch : dans la mesure du possible, catcher l’exception la plus fine possible.
* Retour de fonction : être consistant (toujours une valeur du même type ou None).
