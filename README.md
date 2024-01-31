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

Or simply download it from the link above and put it into the data directory. 

When you have the data downloaded, you can run

```
dvc repro plotting
```

to create several plots visualizing the dataset, all of which will be saved in the plots directory, or

```
dvc repro compare
```

to get the csv fie with the results in the data directory as well as the table with the results printed in python's console.

If you want to customize the year, country and/or any other parameter used in this project, open file 'params.yaml' and change the parameter value accordingly to parameter type.