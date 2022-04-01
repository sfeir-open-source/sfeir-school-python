

<!-- .slide: class="with-code" -->

# Les bases - 12

**Les Librairies standard**

## os

* Librarie permettant de manipuler les path, la lecture et l'ecriture de fichier: 


```python
from os import listdir, path

folder = "folder"
list_files: list[str] = listdir(folder) # List file and folder in specific path (here relative path)
for file_name in list_files: 
    file_path = path.join(folder, file_name) # Concat path of folder and file_name with "/"
    file = open(file_path, mode='r')
    # Reading the file line by line.
    line = file.readlines() # Read line one by one
    while line:
        print(line)
        line = file.readline()
    file.close() # Close file

```


##==##

# Les bases - 12

**Les Librairies standard**

## re

* Librarie permettant de manipuler les regex:

```python
str = "string"
regex_filter = r"^[a-z]" # Match la première lettre

match = re.search(regex_filter, str)
if match:
    print(match.group(0)) # return s
```

##==##

# Les bases - 12

**Les Librairies standard**

## sys

* Librarie permettant de manipuler l'ecosystem python:

```python
# main.py
import sys

print(f"Args used {sys.argv[1]}, {sys.argv[2]}")
    
```

```bash
python3 main.py "test1" "test2" # Output Args used test1 test2
```