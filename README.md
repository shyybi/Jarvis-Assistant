# Jarvis-Assistant

## You don't speak French ? Look for the English branch ! 

### Présentation :
Jarvis est un assistant vocal en python, créer a partir de mon ennuie nocturne et de ma dépression, il est utilisable sur Windows comme Linux, cependant vous devriez installer FFMPEG.

### Installation : 

**Requis :** 

``FFMPEG`` : https://ffmpeg.org/download.html
(le fichier requis est "ffplay")

``Python``: https://www.python.org/

``Pip3``: https://pypi.org/

**Etapes :**

Ouvrir un terminal et entrer la commande : 

``` pip install -r requirements.txt  ```

Après avoir installer FFMPEG et avoir extrait FFPLAY, votre dossier devrais ressembler à ça : 

Jarvis-Assistant -  
|- ffplay   
|- Jarvis.py    
|- README.md    
|_ requirements.txt

Vous pouvez maintenant executer la commande suivante : 

`` python Jarvis.py ``

Si vous souhaitez créer un fichier bash afin de cliquer sur une icon et éviter d'ouvrir un terminal à chaque fois :

- Créer un fichier bash (Windows : .bat / Linux : .sh)

Windows : 
``` 
@echo off       
python Jarvis.py 
pause
```
-------------
Linux :

- Avant, vous devriez éxecuter la commande ``chmod +x run_jarvis.sh``

```
#!/bin/bash
python Jarvis.py
```