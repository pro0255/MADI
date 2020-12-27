from load.load import load_bank_dataset
import numpy as np
import pandas as pd
from atrribute_analyser.Analyser import Analyser

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
        def map_func(value):
            vector = [0] * len(unique)
            index = np.squeeze(np.where(unique == value))
            vector[index] = 1
            return tuple(vector)
        return map_func


    def resize(sefl, dS):
        no = dS[dS['y'] == 'no']
        yes = dS[dS['y'] == 'yes']
        l_yes = len(yes)
        picked_no = dS.loc[0:l_yes, :]
        result = pd.concat([yes, picked_no])
        result = result.sample(frac=1)
        return result


    def encode_values(self, dS):
        #Ordinary data
        dS['education'] = list(map(self.encode_education, dS['education'].values))

        #Nominal data
        unique_jobs = dS.loc[:, 'job'].unique()
        dS['job'] = list(map(self.encode_nominal_data_deps(unique_jobs), dS['job'].values))

        unique_marital = dS['marital'].unique()
        dS['marital'] = list(map(self.encode_nominal_data_deps(unique_marital), dS['marital'].values))

        dS['housing'] = list(map(self.encode_to_binary, dS['housing'].values))
        dS['loan'] = list(map(self.encode_to_binary, dS['loan'].values))
        return dS


    def delete_missing(self, dS):
        #Odstraneni takovych instanci ktere maji unknown... zbytecny sum..
        missing_indicator = 'unknown'
        dS = dS[dS['job'] != missing_indicator]
        dS = dS[dS['education'] != missing_indicator]
        dS = dS[dS['marital'] != missing_indicator]
        return dS




    def preprocess_specific_to_client_attributes(self, dS):
        #size 41 118, crazy to cluster
        client_attributes = ['age', 'job', 'marital', 'education', 'housing', 'loan']
        missing_indicator = 'unknown'

        tmp = dS.loc[:, client_attributes]
        tmp = self.delete_missing(tmp)
        return self.encode_values(tmp)

    def preprocess_client_social_economic(self, dS):
        dS = self.delete_missing(dS)
        dS = self.encode_values(dS)
        client_and_soc_eco_attributes = ['age', 'job', 'marital', 'education', 'housing', 'loan', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']
        return dS.loc[:, client_and_soc_eco_attributes]

        

    def preprocess(self):
        print(f'Preprocessing {type(self).__name__}')
        if self.preprocessed is None:
            if not hasattr(self, 'raw'):
                self.load()
            dS_copy = self.raw.copy()
            # dS_copy = dS_copy.drop(categorial_attributes, axis=1)
            self.preprocessed = self.preprocess_specific_to_client_attributes(self.resize(dS_copy))
        return self.preprocessed

class BankMarketingClient(BankMarketing):
    def preprocess(self):
        print(f'Preprocessing {type(self).__name__}')
        if self.preprocessed is None:
            if not hasattr(self, 'raw'):
                self.load()
            dS_copy = self.raw.copy()
            # dS_copy = dS_copy.drop(categorial_attributes, axis=1)
            self.preprocessed = self.preprocess_specific_to_client_attributes(self.resize(dS_copy))
            analyser = Analyser()
            analyser.analyse_preprocessed_dataset(self.preprocessed, type(self).__name__)
        return self.preprocessed


class BankMarketingClientWithSocialEconomic(BankMarketing):
    def preprocess(self):
        print(f'Preprocessing {type(self).__name__}')
        if self.preprocessed is None:
            if not hasattr(self, 'raw'):
                self.load()
            dS_copy = self.raw.copy()
            # dS_copy = dS_copy.drop(categorial_attributes, axis=1)
            self.preprocessed = self.preprocess_client_social_economic(self.resize(dS_copy))
            analyser = Analyser()
            analyser.analyse_preprocessed_dataset(self.preprocessed, type(self).__name__)
        return self.preprocessed
