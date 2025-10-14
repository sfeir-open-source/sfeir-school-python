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

##==##
# Avant de se lancer

**Performances** (en secondes, fibo=récursivité, bubble=itérations)

| Version   | fibo 1T | vs. 3.14 | bubble 1T | vs. 3.14 | fibo 4T | vs. 3.14 | bubble 4T | vs. 3.14 |
|-----------| ------- | -------- | --------- | -------- | ------- | -------- | --------- | -------- |
| 3.9       | 13.81   | 0.45x    | 3.29      | 0.60x    | 57.51   | 0.46x    | 12.58     | 0.66x    |
| 3.10      | 14.97   | 0.42x    | 3.38      | 0.57x    | 61.57   | 0.43x    | 12.95     | 0.65x    |
| **3.11**  | 9.23    | 0.71x    | 2.15      | 0.91x    | 36.98   | 0.70x    | 7.89      | 0.97x    |
| 3.12      | 8.54    | 0.78x    | 2.46      | 0.82x    | 34.13   | 0.82x    | 9.01      | 0.92x    |
| 3.13      | 8.24    | 0.79x    | 2.61      | 0.78x    | 33.53   | 0.81x    | 9.78      | 0.88x    |
| 3.14      | 6.39    | --       | 2.05      | --       | 24.96   | --       | 8.27      | --       |
| Pypy 3.11 | 1.24    | 4.93x    | 0.14      | 18.14x   | 6.84    | 4.02x    | 0.59      | 16.65x   |
| Node 24   | 1.28    | 4.88x    | 0.21      | 6.64x    | -       | -        | -         | -        |
| Rust 1.90 | 0.10    | 69.82x   | 0.07      | 36.15x   | -       | -        | -         | -        |
