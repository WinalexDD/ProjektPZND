# ProjektPZND

Project bases on dataset about suicides from kaggle: 
https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016

The aim is to choose the best regression model to predict the suicide number.
In order to do that, we will create several regression models and evaluate their accuracy basing on the r^2 score.

## How to run this project

### Setting up virtual environment and installing requirements

After cloning the repository set up virtual environment:

In Windows (the author's setup):

```
python -m venv venv 
venv/Scripts/activate
pip install -r requirements.txt
```

In Linux:

```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

### Runing the project:

This project uses Data Version Control (knows as DVC) to oversee our dataset. 
To download it either set-up password to remote SSH storage, and pull the data:

```
dvc remote modify --local ssh-storage password [put_password_here]
dvc pull
```

Or simply download it from the link above and put it into the data directory. When you have the data downloaded, you can make this project do two functionalities: 

The first one is about data plotting. You start by typing:

```
dvc repro plotting
```

in terminal to create several plots visualizing the dataset, all of which will be saved in the plots directory and then input:

 ```
dvc plots show
```

to create a html file printing all of said plots. 

The second one is about said regression comparison, which can be initiated by:

```
dvc repro compare
```

that will produce a csv file with the results as well as txt file containing the table with the results, that will also be printed in python's console. Both of these files, together with several other data files used in previous steps will be saved in the data directory with corresponding names. You can also run every single previous stage of the project, by dvc repro "name", or just run every single file by itself to see its functionality. The stage names and the files order of running can be seen by user in dvc.yaml file and through imports/loads in the .py files.

You can then also customize the parameters used in this project, such as the year, country and/or multiple others, by opening file 'params.yaml', changing the parameters value accordingly to their type and then reruning the part of the project where this parameter is used. 