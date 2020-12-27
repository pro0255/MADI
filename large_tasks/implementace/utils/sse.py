from utils.distance import calc_distance

def sse(centroid, cluster):
    error = 0
    for instance in cluster:
        d = calc_distance(instance, centroid)
        error += d
    return error

def total_sse(centroid2Cluster):
    total_sse = 0
    for centroid, cluster in centroid2Cluster.items():
        error = sse(centroid, cluster)
        total_sse += error
    return total_sse