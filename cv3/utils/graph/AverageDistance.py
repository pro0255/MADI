def average_distance(floyd_matrix, verbose=False):
    n = len(floyd_matrix)
    sum = 0
    for i in range(n):
        for j in range(i, n):
            sum += floyd_matrix[i][j]
    result = (2/(n*(n-1)))*sum

    o =  f'Prumerna vzdalenost - {result}'

    output = f'{o}\n'
    if verbose:
        print(o)
    return (output, result)