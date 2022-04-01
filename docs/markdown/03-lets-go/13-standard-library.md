

<!-- .slide: class="with-code" -->

# Les bases - 12

**Les Librairies standard**

## os

* Librarie permettant de manipuler les path, la lecture et l'ecriture de fichier: 


```python
import os

list_files: list[str] = os.listdir(folder)
for file in files: 
    reader = os.open(file, "rt")
    line = reader.readlines()
    while line:
        print(line)
    os.close(file)
    
```

<!-- .element: class="big-code" -->


##==##

# Les bases - 12

**Les Librairies standard**

## re

* Librarie permettant de manipuler les regex:

# TODO valid it 
```python
import re

str = "string"
regex_filter = r"^[a-z]" # Match la première lettre

match = re.search(regex_filter, str)
if match:
    return match.group(0) # return s
    
```

##==##

# Les bases - 12

**Les Librairies standard**

## sys

* Librarie permettant de manipuler l'ecosystem python:

# TODO valid it 
```python
# main.py
import sys

print(f"Args used {sys.argv[1]}, {sys.argv[2]}")
    
```

```bash
python3 main.py "test1" "test2" # Output Args used test1 test2
```

# TODO add exercice and correction