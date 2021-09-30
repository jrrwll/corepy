from time import perf_counter as pc
from unittest import TestCase

from corepy.matrix import Matrix, pascal


class TestMatrix(TestCase):

    def test_pascal_large(self):
        for i in range(1, 36):
            A = Matrix(i, i)
            A.data = pascal(i)
            det = A.det()
            print("%2d-level pascal det is %.8G" % (i, det))

    def test_pascal(self):
        i = 12
        A = Matrix(i, i)
        A.data = pascal(i)
        print("before")
        A.pretty()
        t = pc()
        det = A.det()
        t = pc() - t
        print("after")
        A.pretty()
        print("%2d-level pascal det is %.8G, cost %.3fus" % (i, det, t * 10 ** 6))
