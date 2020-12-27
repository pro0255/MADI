from load.load import load_bank_dataset
import numpy as np

numeric_attributes = ['age', 'duration', 'campaign', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']

categorial_attributes = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome', 'y']

class BankMarketing:
    def __init__(self):
        self.preprocessed = None

    def load(self):
        print(f'Loading {type(self).__name__}')
        self.raw = load_bank_dataset()


    def get_preprocessed_features(self):
        if self.preprocessed is None:
            self.preprocess()
        return self.preprocessed.columns


    def preprocess_social_economic_attributes(self, dS):
        """A lot of same values"""
        return dS.loc[:, ['emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']]

    def preprocess_drop_categorical(self, dS):
        """To much time to cluster this kind of data"""
        return dS_copy.drop(categorial_attributes, axis=1)

    def encode_to_binary(self, value):
        if value == 'yes':
            return 1
        else:
            return 0



    def encode_education(self, value):
        if value == 'illiterate':
            return 0
        elif value == 'basic.4y':
            return 1
        elif value == 'basic.6y':
            return 2
        elif value == 'basic.9y':
            return 3
        elif value == 'high.school':
            return 4
        elif value == 'professional.course':
            return 5
        elif value == 'university.degree':
            return 6


    def encode_nominal_data_deps(self, unique):
        print(unique)
        def map_func(value):
            vector = [0] * len(unique)
            index = np.squeeze(np.where(unique == value))
            vector[index] = 1
            return vector
        return map_func




    def preprocess_specific_to_client_attributes(self, dS):
        client_attributes = ['age', 'job', 'marital', 'education', 'housing', 'loan']
        missing_indicator = 'unknown'

        tmp = dS.loc[:, client_attributes]

        #Odstraneni takovych instanci ktere maji unknown... zbytecny sum..
        tmp = tmp[tmp['job'] != missing_indicator]
        tmp = tmp[tmp['education'] != missing_indicator]
        tmp = tmp[tmp['marital'] != missing_indicator]


        #Ordinary data
        tmp['education'] = list(map(self.encode_education, tmp['education'].values))


        #Nominal data
        unique_jobs = tmp.loc[:, 'job'].unique()
        tmp['job'] = list(map(self.encode_nominal_data_deps(unique_jobs), tmp['job'].values))

        unique_marital = tmp['marital'].unique()
        tmp['marital'] = list(map(self.encode_nominal_data_deps(unique_marital), tmp['marital'].values))

        tmp['housing'] = list(map(self.encode_to_binary, tmp['housing'].values))
        tmp['loan'] = list(map(self.encode_to_binary, tmp['loan'].values))

        return tmp

    def preprocess(self):
        print(f'Preprocessing {type(self).__name__}')
        if self.preprocessed is None:
            if not hasattr(self, 'raw'):
                self.load()
            dS_copy = self.raw.copy()
            # dS_copy = dS_copy.drop(categorial_attributes, axis=1)

            self.preprocessed = self.preprocess_specific_to_client_attributes(dS_copy)
        return self.preprocessed