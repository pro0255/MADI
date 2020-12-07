import pandas as pd

def get_weather_set():
    weather_data = pd.read_csv('weather.csv', ';')
    X = weather_data.drop('Play', axis=1)
    y = weather_data['Play']
    return X, y

def get_bank_set():
    ##https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
    bank = pd.read_csv('bank-additional-full.csv', ';')
    bank_categorical_X = bank[['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']]
    bank_categorical_y = bank['y']
    return bank_categorical_X, bank_categorical_y
