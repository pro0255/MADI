from load.load import load_mall_customers_dataset
from atrribute_analyser.Analyser import Analyser
from CONSTANTS import MAKE_ATTRIBUTE_ANALYSIS


class MallCustomers:
    def __init__(self):
        self.preprocessed = None

    def load(self):
        print(f'Loading {type(self).__name__}')
        self.raw = load_mall_customers_dataset()

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
            dS_copy = dS_copy.drop(['CustomerID', 'Gender'], axis=1)
            self.preprocessed = dS_copy
            if MAKE_ATTRIBUTE_ANALYSIS:
                analyser = Analyser()
                analyser.analyse_preprocessed_dataset(self.preprocessed, type(self).__name__)
        return self.preprocessed