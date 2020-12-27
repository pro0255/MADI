import os
import CONSTANTS
from utils.analyse_numeric import attribute_variance, attribute_mean, global_mean, global_variance


class Analyser():
    def __init__(self, path=CONSTANTS.GLOBAL_PATH_TO_ANALYSIS):
        self.path = path


    def create_path(self, directory):
        return f'{self.path}//{directory}'


    def create_directory(self, directory):
        if not os.path.exists(self.create_path(directory)):
            os.makedirs(self.create_path(directory))

    def analyse_preprocessed_dataset(self, dS, directory):
        print('Running analysis')
        self.create_directory(directory)
        ok_attributes = []
        for c in dS.columns:
            feature = dS.loc[:, c]
            try:
                mean = attribute_mean(feature)
                variance = attribute_variance(feature)
                ok_attributes.append(c)
            except Exception as e:
                pass
                # print(f'cannot calculate mean')
                # print(e)

        subdS = dS.loc[:, ok_attributes]
        print(subdS.head())
        average_instance = global_mean(subdS)
        g_var = global_variance(subdS)
        print(average_instance)
        print(g_var)
    