# Cataloging-and-Visualising-Cradles-of-Planet-Formation

## Project description

Circumstellar disks composed of dust and gas are the natural outcome of stellar formation. They are the places where planetary systems are formed through a variety of physical processes.
In the past 5 years we have opened the possibility to observe these disks at high spatial resolution in scattered light. For this purpose we use the largest ground based telescopes in conjucture with new extreme adaptive optics instruments in the optical and near infrared. These new observations have revealed a plethora of features in these circumstellar disks from large cavities, to small rings and gaps and even huge spiral arms. All of these features are thought to be signposts of ongoing planet formation.

Recently the first VLT/SPHERE survey of such disks came to a conclusion. At the same time a new program lead by researchers from Amsterdam and Leiden University is about to start that will significantly extend the sample of resolved disks. The student will be introduced to the concept of scattered light imaging. The goal is to assemble a complete catalog of all such observation that were conducted and published to date. The catalog will be combined with a web interface for easy access and basic statistical analysis.
The goal is on the one hand to design an efficient tool for researchers, which can be easily queried, maintained and updated, and on the other hand a visualisation experience for a general audience. One possibility that can be explored would be the (simplified) 3d reconstruction of circumstellar disks from 2d data.

A research blog to track my work done can be found [here](https://rywjhzd.github.io/year-archive/). 
The database is created with Django and DataTables. Disk models make uses of threejs.org and Lee Stemkoski's three.js examples. 

## Run the database

* Clone this repository. 
* Create a virtual environment with Python 3.
* Activate the virtual environment. 
* Install the dependencies.
* Migrate the database.
* Load http://localhost:8000/ to access the database. 

```
git clone https://github.com/rywjhzd/Cataloging-and-Visualising-Cradles-of-Planet-Formation.git
cd Cataloging-and-Visualising-Cradles-of-Planet-Formation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py runserver
```
## Data
After the server is hosted. 
* Load http://localhost:8000/admin/ to the administration page. 
* Put in the username and password. 
* Click *Disks* and then there should be an *Import* and an *Export* button.
* Click either and follow the instruction. 

Note: when importing files, make sure *id* is not duplicated. This column can be edited manually.

## Display the disk
disk_model.html contains the model and disk_model_test.html is to test scripts.
```
cd Cataloging-and-Visualising-Cradles-of-Planet-Formation/diskmodel
open disk_model.html
```
