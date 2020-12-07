import random

def train_test_split(X, y, float_per):
    """Method split dataset to two parts, one is set for purpose of train and secound is for testing. After testing we could calculate accurency of created model.
    Args:
        data (DataFrame): Loaded dataframe.
        float_per (float): Represents size of test data.
    Returns:
        [tuple]: Splited input dataset to two parts (train, test).
    """
    seed = random.randint(0, 100)

    n = len(X)

    shuffled_X = X.sample(frac=1, replace=True, random_state=seed) 
    shuffled_y = y.sample(frac=1, replace=True, random_state=seed)

    split_size = int(n * float_per)

    X_test = shuffled_X[0:split_size] 
    X_train = shuffled_X[split_size:]

    y_test = shuffled_y[0:split_size] 
    y_train = shuffled_y[split_size:]

    return (X_train, y_train, X_test, y_test) 



    
