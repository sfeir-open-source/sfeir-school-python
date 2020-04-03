<!-- .slide: class="with-code" -->

# Les bases - 03

**Les chaînes de caractères**

```python
print('ma chaine')  # ma chaine
print(“ma chaine”)  # ma chaine

print('''ma         # ma
chaine''')            chaine
```

<!-- .element: class="big-code" -->

Notes:
Il est possible de créer des chaînes de caractères avec des simples ou des double quotes. La seule contrainte est de fermer les chaînes de caractères de la même manière qu’on les ouvre. (Python ne recommande pas une ou l’autre manière de faire, juste de rester cohérent avec toutes la base de code déjà disponible, si vous utilisez des doubles quotes, continuez, n’allez pas changer maintenant).Point intéressant, en Python vous pouvez créer des chaînes multilignes. Elles commencent par trois quotes (ou double quotes), et se finissent de la même manière. Toute chaîne de caractères définie ainsi, garde le formatage qui a été employé (saut de ligne, espaces en début de lignes, tabulation…)

##==##
<!-- .slide: class="with-code" -->

# Les bases - 03

**Opérations sur les string**

```python
'ma chaine'.split(' ')  # ['ma', 'chaine']
' '.join(['ma', 'chaine'])  # ma chaine
'ma chaine'.find('c')  # 3
'ma chaine'.upper()  # MA CHAINE
```

<!-- .element: class="big-code" -->

Notes:
On retrouve les opérations classiques sur les chaînes (split, join, find, case change…)

##==##
<!-- .slide: class="with-code" -->

# Les bases - 03

**Formatage sur les string**

```python
str1 = 'ma'
str2 = 'chaine'
str1 + str2  # machaine
'{} {}'.format(str1, str2)  # ma chaine
'{0} {1}'.format(str1, str2)  # ma chaine
'{p1} {p2}'.format(p1=str1, p2=str2)  # ma chaine
f'{str1} {str2}' # ma chaine
```

<!-- .element: class="big-code" -->

Notes:
Il y a beaucoup de façon en Python d’appliquer un format sur des chaînes, voir de les concaténer.Vous avez ici un panel de ce qui est possible de faire. Je vous recommande la dernière option, apparue en Python3 qui est tout de suite plus parlante et plus lisible.

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Les bases - 03

**Opérations sur les string**

##--##

<br>

```python
a = 'ma chaine'
a[:2]  # ma
a[3:]  # chaine
a[::3]  # mci
a[::-2]  # eih m
a[:]  # ma chaine
```

##--##

<br>

```python
len(a)  # 9
a.count('a')  # 2
```

##==##
<!-- .slide: class="with-code two-column-layout" -->

# Les bases - 03

**Opérations sur les string unicode**

##--##

<br>

```python
s = '字'

len(s)  # 3
s  # '\xe5\xad\x97'
print s  #  字
```

##--##

<br>

```python
w = s.decode('utf-8')
w  # u'\u5b57'
print w  # 字

z = s.decode('latin-1')
z  # u'\xe5\xad\x97'
print z  # å
```
