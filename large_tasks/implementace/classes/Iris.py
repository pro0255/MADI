from load.load import load_iris_dataset
from atrribute_analyser.Analyser import Analyser

class Iris:
    def __init__(self):
        self.preprocessed = None

    def load(self):
        print(f'Loading {type(self).__name__}')
        self.raw = load_iris_dataset()


    def get_preprocessed_features(self):
        if self.preprocessed is None:
            self.preprocess()
        return self.preprocessed.columns


    def preprocess(self):
        print(f'Preprocessing {type(self).__name__}')
        if self.preprocessed is None:
            if not hasattr(self, 'raw'):
                self.load()
            dS_copy = self.raw.copy()
            dS_copy = dS_copy.drop(['variety'], axis=1) 
            for index, value in dS_copy.items():
                dS_copy.loc[:, index] = value.str.replace(',', '.').astype(float)
            self.preprocessed = dS_copy
            analyser = Analyser()
            analyser.analyse_preprocessed_dataset(self.preprocessed, type(self).__name__)
        return self.preprocessed