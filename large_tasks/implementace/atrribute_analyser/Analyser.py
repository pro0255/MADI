import os
import CONSTANTS
from utils.analyse_numeric import attribute_variance, attribute_mean, global_mean, global_variance, draw_distribution, draw_cdf


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

        columns_text = ''
        for c in dS.columns:
            feature = dS.loc[:, c]
            try:
                mean = attribute_mean(feature)
                variance = attribute_variance(feature)
                columns_text += f"\t{c}\n\t\tmean = {mean}\n\t\tvariance = {variance}\n"
                f1,ax1 = draw_distribution(feature, mean, variance, c)
                f2,ax2 = draw_cdf(feature, mean, variance, c)
                f1.savefig(f'{self.create_path(directory)}//{c}_pdf.png')
                f2.savefig(f'{self.create_path(directory)}//{c}_cdf.png')
                ok_attributes.append(c)
            except Exception as e:
                pass
                print(f'cannot calculate mean')
                print(e)

        subdS = dS.loc[:, ok_attributes]
        average_instance = global_mean(subdS)
        g_var = global_variance(subdS)




        text = f'Data set with:\n\tSize = {len(dS)}\n{columns_text}\n\tAttributes which were numeric or binary: {ok_attributes}\n\taverage instance = {average_instance}\n\tglobal variance = {g_var}'
        with open(f'{self.create_path(directory)}//text_output.txt', 'w') as f:
            f.write(text)    



    