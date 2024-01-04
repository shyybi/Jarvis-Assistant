# Jarvis-Assistant

## Tu ne parle pas Anglais ? Regarde la branch en Français (main) !

### Introduction:
Jarvis is a Python voice assistant, created out of my nocturnal boredom and depression. It can be used on both Windows and Linux, however, you should install FFMPEG.

### Installation:

**Requirements:**

`FFMPEG`: https://ffmpeg.org/download.html
(The required file is "ffplay")

`Python`: https://www.python.org/

`Pip3`: https://pypi.org/

**Steps:**

Open a terminal and enter the command:

``` pip install -r requirements.txt  ```

After installing FFMPEG and extracting FFPLAY, your folder should look like this:

Jarvis-Assistant -  
|- ffplay   
|- Jarvis.py    
|- README.md    
|_ requirements.txt

You can now execute the following command:

`` python Jarvis.py ``

If you want to create a bash file to click on an icon and avoid opening a terminal each time:

- Create a bash file (Windows: .bat / Linux: .sh)

Windows : 
``` 
@echo off       
python Jarvis.py 
pause
```
-------------
Linux :

- Before, you should execute the command ``chmod +x run_jarvis.sh``

```
#!/bin/bash
python Jarvis.py
```
