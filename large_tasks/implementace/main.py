import pandas as pd
from load.load import load_bank_dataset, load_iris_dataset
from utils.analyse_categorical import analyse_categorial
from utils.analyse_numeric import analyse_numeric
from classes.Iris import Iris
from gui.App import Application



#TODO: 
# - make analysis for every attribtute
# - preprocessing data
# - create GUI for application


categorial_attributes = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome', 'y']
numeric_attributes = ['age', 'duration', 'campaign', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']

def start_analysis_on_categorical_attributes(data_set, method):
    [method(data_set, c_name) for c_name in data_set.columns]

# iris = Iris()
# iris.load()

# dS = iris.preprocess()
# start_analysis_on_categorical_attributes(dS, analyse_numeric)
# start_analysis_on_categorical_attributes(dS, categorial_attributes, analyse_categorial)


app = Application()
app.start(False)




