from load.load import load_iris_dataset

class Iris:
    def __init__(self):
        print('constructing iris')

    def load(self):
        print(f'Loading {type(self).__name__}')
        self.raw = load_iris_dataset()

    def preprocess(self):
        print(f'Preprocessing {type(self).__name__}')
        dS_copy = self.raw.copy()
        dS_copy = dS_copy.drop(['variety'], axis=1) 
        for index, value in dS_copy.items():
            dS_copy.loc[:, index] = value.str.replace(',', '.').astype(float)
        return dS_copy