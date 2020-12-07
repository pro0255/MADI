from collections import Counter
import numpy as np
class NaiveBayers():
    def __init__(self):
        self.class_dic = {}
        self.class2probDic = {}
        self.prior_probability = {}

    def fit(self, X, y):
        n_X = X.to_numpy()
        n_y = y.to_numpy()
        number_of_features = n_X.shape[1] 
        self.class_dic = dict(y.value_counts())
        s = np.sum(list(self.class_dic.values()))
        self.prior_probability = {k:(v/s) for k,v in self.class_dic.items()}

        for class_index, classificator in enumerate(self.class_dic.keys()):
            indicies = np.where(n_y == classificator)
            sub_set = np.squeeze(n_X[indicies, :])
            denominator = self.class_dic[classificator]
            self.class2probDic[class_index] = {}

            for feature_index in range(number_of_features):
                feature_counter = Counter(sub_set[:, feature_index])
                feature_probability = {k:(v/denominator) for k,v in feature_counter.items()}
                self.class2probDic[class_index][feature_index] = dict(feature_probability)

    def predict_instance(self, instance):
        prediction_vector = []
        for class_index, prior_prob in enumerate(self.prior_probability.values()):
            result = [prior_prob]
            for col_i, value in enumerate(instance):
                if value in self.class2probDic[class_index][col_i]:
                    result.append(self.class2probDic[class_index][col_i][value])

            prediction_vector.append(np.prod(result))
        return np.array(prediction_vector)


    def construct_label_prediction(self, predictions_vector):
        labels_vector = []
        labels = list(self.class_dic.keys())
        for vector in predictions_vector:
            label_index = np.argmax(vector)
            labels_vector.append(labels[label_index])
        return labels_vector

    def predict(self, X):
        n_X = X.to_numpy()
        prediction_result = []
        for instance in n_X:
            prediction_result.append(self.predict_instance(instance))

        labeled_prediction = self.construct_label_prediction(prediction_result)
        return labeled_prediction, np.array(prediction_result) 