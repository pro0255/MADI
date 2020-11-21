import pandas as pd
from constants.CONSTANTS import COLUMNS_IN_ROW



class GmailParser():
    def __init__(self):
        pass

    def parse(self, path_to_file, names=COLUMNS_IN_ROW):
        raw_gmail_data = pd.read_csv(path_to_file, delimiter=';', encoding='unicode_escape', header=None)
        raw_gmail_data.columns = names
        self.clean_data(raw_gmail_data)

    def clean_data(data, raw_data):
        print(raw_data.head())
        print(raw_data.iloc[0])
    
 