from array import array


def pascal(m, n=None):
    if not n:
        n = m
    v = [array('d', [1 for j in range(n)]) for i in range(m)]
    # v = [[1 for i in range(m)] for j in range(n)]
    for i in range(1, m):
        for j in range(1, n):
            if i == 0 or j == 0:
                v[i][j] = 1
            else:
                v[i][j] = v[i - 1][j] + v[i][j - 1]
    return v


def hilb(dim):
    return [[1 / (i + j + 1) for i in range(0, dim)] for j in range(0, dim)]
