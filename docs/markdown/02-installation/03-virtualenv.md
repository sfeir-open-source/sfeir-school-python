# Installation de l’environnement

**Installation de virtualenv**

* Création d'environnements Python isolés, sans conflits de versions : https://virtualenv.pypa.io/en/stable/
* `$ python3 -m pip install virtualenv`
* `$ virtualenv --version`

Notes:
En Python, les librairies tierses sont installées dans un répertoire inscrit dans votre version de Python. Sauf que (contrairement au Java), elles ne sont pas sauvegardées et triées en fonction de leur version. Par conséquent, on ne peut pas installer 2 versions différentes d’une lib dans ce répertoire partagé de Python (enfin si, on peut, mais je ne garantis pas le résultat). Si votre projet X dépend de la version 1 d’une lib, et votre projet Y de la version 2 de cette même lib, et que vous procédez à l’install de la version 1 et de la version 2, vous finirez par avoir des conflits et des résultats incohérents dans vos 2 projets.C’est pour cela qu’en Python, vous entendrez souvent parler du terme “Virtual Environment”. Concrétement, il s’agit d’un dossier dans votre projet qui servira à isoler vos dépendances tierses du reste du répertoire commun de python. Vous pouvez même isoler votre version de Python directement et avoir un projet en 3.7 et un autre en 3.8 !Pour l’installer : python3 -m pip install virtualenv
