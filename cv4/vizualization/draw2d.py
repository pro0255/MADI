import matplotlib.pyplot as plt
import numpy as np

def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)

def draw2d(ind2Cluster, centroids, index_attributes):
    f, ax = plt.subplots(figsize=(10,6))
    ax.grid()
    ax.title.set_text('K means')

    i1 = index_attributes[0] #vizulazed x
    i2 = index_attributes[1] #vizulazed y


    cluster_matricies = [np.squeeze(cluster) for cluster in ind2Cluster.values()]

    pickedX = [matrix[:, i1] for matrix in cluster_matricies]
    pickedY = [matrix[:, i2] for matrix in cluster_matricies]

    cX = centroids[:, i1]
    cY = centroids[:, i2]

    k = len(pickedX)

    colors = np.random.rand(k,3)
    for index in range(k):
        color = colors[index] 
        ax.scatter(pickedX[index], pickedY[index], c=color, s=20)
        ax.scatter(cX[index], cY[index], c="black", s=100, marker="D")

    

    plt.show()