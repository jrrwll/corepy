from unittest import TestCase

import numpy
from matplotlib import pyplot

from . import PID


class TestPID(TestCase):
    def test_PID(self):
        # X = numpy.linspace(-numpy.pi, numpy.pi, 256, endpoint=True)
        # C, S = numpy.cos(X), numpy.sin(X)
        # pyplot.plot(X, C)
        # pyplot.plot(X, S)

        p = PID(-1.0, -0.02, 0.05, -1500.0)
        X = numpy.linspace(0, numpy.pi, 100, endpoint=True)
        for i in range(99):
            p.progress()
        pyplot.plot(X, numpy.array(p.EV))
        pyplot.show()

    def test_PID_no_integral_filter(self):
        p = PID(-1.0, -0.02, 0.05, -1500.0, False)
        X = numpy.linspace(0, numpy.pi, 100, endpoint=True)
        for i in range(99):
            p.progress()
        pyplot.plot(X, numpy.array(p.EV))
        pyplot.show()
