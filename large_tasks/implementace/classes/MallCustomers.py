from load.load import load_mall_customers_dataset

class MallCustomers:
    def __init__(self):
        print('constructing iris')
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
        return self.preprocessed