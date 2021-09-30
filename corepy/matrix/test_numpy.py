from time import time
from unittest import TestCase

import numpy
from matplotlib.pyplot import plot, show

from corepy.matrix import Matrix, pascal


class TestNumpy(TestCase):
    def test_speed_only(self):
        matrix_ts = []
        r = range(1, 65)
        for i in r:
            A = Matrix(i, i)
            A.data = pascal(i)

            ts1 = time()
            det1 = A.det()
            ts1 = time() - ts1
            matrix_ts.append(ts1)

            print("%2d\tdet:\t%.8G, cost:\t%.3f" % (i, det1, ts1 * 1000))

        plot(r, matrix_ts, 'r-')
        show()

    def test_speed(self):
        matrix_ts = []
        numpy_ts = []
        r = range(1, 34)
        for i in r:
            A = Matrix(i, i)
            A.data = pascal(i)

            ts1 = time()
            det1 = A.det()
            ts1 = time() - ts1
            matrix_ts.append(ts1)

            ts2 = time()
            a = numpy.core.numeric.asarray(pascal(i))
            det2 = numpy.linalg.det(a)
            ts2 = time() - ts2
            numpy_ts.append(ts2)

            print("%2d\t[matrix, numpy] det:\t%.8G, %.8G, cost:\t%.3f, %.3f" % (
                i, det1, det2, ts1 * 10 ** 6, ts2 * 10 ** 6))

        plot(r, matrix_ts, 'r-', r, numpy_ts, 'g-.')
        show()
