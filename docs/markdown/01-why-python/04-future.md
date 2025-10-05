# Avant de se lancer

**L’avenir de Python**

* Python 2.x n'est plus maintenu depuis 2020.
* Migration vers 3.10+ recommandée.
* Python 3.14 sortie le 7 octobre 2025.

Notes:
Vous verrez très souvent des projets utilisant Python2. Cependant il est déconseillé de démarrer de nouveaux projets avec cette version de Python. En effet, à compter du 1er Janvier 2020, cette version n’est plus du tout maintenue, et la migration en Python 3 est conseillée, et ce afin de bénéficier des dernières évolutions et des derniers correctifs de sécurités.Dans cette formation, nous utiliserons une version de Python supérieure ou égale à 3.7.

En moyenne, Python 3.11 est plus 1,22 fois plus rapide que Python 3.10. Mais ce gain peut aller entre 1,1 et 1,6 en fonction de la tâche.

##==##

<!-- .slide: class="with-code" -->
# Avant de se lancer

**Python 3.14**

* Suggestion de correction sur des fautes de frappe
```python
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(mon_texte.uppper())
AttributeError: 'str' object has no attribute 'uppper'. Did you mean: 'upper'?
```
* Plus rapide, encore et toujours.
* t-strings (Template Strings comme Jinja)
```python
from string import Template
gabarit_message = Template("Bienvenue à $nom qui nous vient de $ville !")
message_pour_alice = gabarit_message.substitute(nom="Alice", ville="Paris")
message_pour_bob = gabarit_message.substitute(nom="Bob", ville="Lyon")
print(message_pour_alice)
print(message_pour_bob)
```

Notes:
Permet a l'IDE de connaitre le type attendu. Affiche un warning si le type n'est pas string ou si s peut être null.
Les hints viennent de la librairie standard typing
