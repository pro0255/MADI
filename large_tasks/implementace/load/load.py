import pandas as pd
import os


def data_set_info(ds):
    print(ds.head())
    print(ds.info())


def load_bank_dataset():
    name_of_file = 'bank-additional-full.csv' 
    bank_marketing = pd.read_csv(f'data_sets\\bank_marketing\\{name_of_file}',  delimiter=';')
    data_set_info(bank_marketing)
    return bank_marketing


def load_iris_dataset():
    name_of_file = 'iris.csv' 
    iris = pd.read_csv(f'data_sets\\iris\\{name_of_file}',  delimiter=';')
    data_set_info(iris)
    # iris = iris.drop(['variety'], axis=1) 
    # for index, value in iris.items():
    #      iris.loc[:, index] = value.str.replace(',', '.').astype(float)
    return iris










