from collections import defaultdict
from utils.distance import calc_distance
from utils.average_instance import calc_average_instance
import numpy as np

def init_k_means(data, k):
    """Picks random instances from data set where every is unique.
    """
    centroids = data.sample(k)
    return centroids


def create_new_centroids(k, ind2Cluster, number_of_features):
    new_centroids = []
    for index_of_cluster in range(k):
        points = np.squeeze(ind2Cluster[index_of_cluster])
        new_centroids.append(calc_average_instance(points, number_of_features))
    return np.array(np.squeeze(new_centroids))

def did_moved(old_centroids, new_centroids):
    comparison = old_centroids == new_centroids
    return not comparison.all()

def k_means(data, k):
    """Starts k-means algorithm with specified hyperparametr k. And data which will be clustered.
    """
    init_centroids = init_k_means(data, k)
    centroids = init_centroids.to_numpy()
    dataset = data.to_numpy()
    number_of_features = dataset.shape[1]  

    ind2Cluster = defaultdict(list) #represents current clusters for specified index of centroid his data, it is used for calculation of new centroids. 
    centroid2Cluster = {}

    while True:
        ind2Cluster.clear()
        centroid2Cluster = {tuple(c):list() for c in centroids}
        for instance in dataset:
            instance2Centroid = []
            for centroid in centroids:
                instance2Centroid.append(calc_distance(instance, centroid))

            closest_centroid_index = np.argmin(instance2Centroid)
            ind2Cluster[closest_centroid_index].append(instance)
            centroid2Cluster[tuple(centroids[closest_centroid_index])].append(instance)

        new_centroids = create_new_centroids(k, ind2Cluster, number_of_features)
        if not did_moved(centroids, new_centroids):
            # print('did not moved')
            break
        centroids = new_centroids

    return (ind2Cluster, centroids, centroid2Cluster)