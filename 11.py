def get_mat(n,m,value):
    mat_ = []
    if n == 0 or m == 0:
        return mat_
    for row in range(n):
        mat_.append([])
        for col in range(m):
            mat_[row].append(value)
    return mat_
print(get_mat(2,3,6))

