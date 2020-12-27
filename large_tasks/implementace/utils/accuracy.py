from collections import Counter

def accuracy_score(predicted, test):
    comparison_vector = predicted == test
    print(comparison_vector)
    c = Counter(comparison_vector)
    result =  c[True]/len(comparison_vector)
    return result


