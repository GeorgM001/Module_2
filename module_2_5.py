def get_matrix(n,m,value):
    matrix = []
    if n == 0 or m == 0:
        return matrix
    for row in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
print(get_matrix(3,2,3))
    