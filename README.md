# IEOR E4501 Final Project
# Squirrel Tracker: a visulization web-application of tracking squirrels


## Introduction

We used Django, a web-application tools which can manage import, modify data, to construct a **Squirrel Tracker** with the  visualization of sightings of squirrels found in Manhattan, New York.


## DataSet
In this project,[**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) dataset, published by [**Squirrel Census**](https://www.thesquirrelcensus.com/) was used to conduct this project.  
This data set contains data 3,023 sightings, including location coordinates, age, primary and so on. 


## Management Commands
Import: is a command that can import the data from the csv file, 2018 Central Park Squirrel Census in this project. Specifically, file path should be included at the command line after the management command. 

```sh
python manage.py import_squirrel_data /path/to/file.csv
```

Export: is a command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv

