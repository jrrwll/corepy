def pascal(m, n=None):
    if not n:
        n = m
    v = [[1 for i in range(m)] for j in range(n)]
    for i in range(1, m):
        for j in range(1, n):
            if i == 0 or j == 0:
                v[i][j] = 1
            else:
                v[i][j] = v[i - 1][j] + v[i][j - 1]
    return v
