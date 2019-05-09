from . import Matrix, pascal

from unittest import TestCase


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
        det = A.det()
        print("after")
        A.pretty()
        print("%2d-level pascal det is %.8G" % (i, det))
