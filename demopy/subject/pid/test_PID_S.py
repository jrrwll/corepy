from unittest import TestCase

import numpy
from matplotlib import pyplot

from ._PID_S import PID_S


class TestPID(TestCase):
    def test_pPID(self):
        # X = numpy.linspace(-numpy.pi, numpy.pi, 256, endpoint=True)
        # C, S = numpy.cos(X), numpy.sin(X)
        # pyplot.plot(X, C)
        # pyplot.plot(X, S)

        p = PID_S(-0.8, 0.15, 0.00, numpy.pi / 100, 1500.0, 0)
        X = numpy.linspace(0, numpy.pi, 100, endpoint=True)
        for i in range(99):
            p.progress()
            print(p.UV[-1])
        pyplot.plot(X, numpy.array(p.UV))
        pyplot.show()
