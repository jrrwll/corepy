from .matrices import *


# slow than numpy, no use in product environment
class Matrix():
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
        self.data = [[0 for i in range(dim1)] for j in range(dim2)]

    def __getitem__(self, item):
        return self.data[item]

    def minDimensions(self):
        return self.dim1 if self.dim1 < self.dim2 else self.dim2

    def det(self):
        ok = self.diagonalize()
        if not ok:
            return 0

        dim = self.minDimensions()
        result = 1
        for k in range(dim):
            result *= self.data[k][k]

        return result

    def diagonalize(self):
        sign = 1
        dim = self.minDimensions()
        for k in range(dim - 1):
            if not self.data[k][k]:
                swapped = False
                # swap rows to make it no-zero
                for i in range(k + 1, dim):
                    if self.data[i][i]:
                        self.swap_row(k, i)
                        swapped = True
                        break
                # if not swapped
                if not swapped:
                    return False

            # this[k][k] will not equal zero in this area
            for i in range(k + 1, dim):
                self.add_other_row(i, k, -self.data[i][k] / self.data[k][k])
        return True

    def add_other_row(self, toIndex, fromIndex, multiple):
        for j in range(self.dim2):
            self.data[toIndex][j] += multiple * self.data[fromIndex][j]

    def swap_row(self, i1, i2):
        for j in (self.dim2):
            tmp = self.data[i1][j]
            self.data[i1][j] = self.data[i2][j]
            self.data[i2][j] = tmp

    def pretty(self):
        for i in range(self.dim1):
            for j in range(self.dim2 - 1):
                print("%.6G" % self.data[i][j], end=", ")
            print("%.6G" % self.data[i][self.dim2 - 1])
