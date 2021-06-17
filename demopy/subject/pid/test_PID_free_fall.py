from unittest import TestCase

import numpy
from matplotlib import pyplot

from . import PID


class FreeFall(TestCase):

    def fix(self, E):
        return E + self.air_resistance(E)

    def air_resistance(self, E):
        return - E ** 2 * 0.03 + 0.1

    def test_PID(self):
        p = PID(-0.8, -0.05, 0.0, -1500.0)
        p.fix = lambda E: self.fix(E)

        X = numpy.linspace(0, numpy.pi, 100, endpoint=True)
        for i in range(99):
            p.progress()
        pyplot.plot(X, numpy.array(p.EV))
        pyplot.show()

    def test_PID_no_integral_filter(self):
        p = PID(-0.8, -0.05, 0.0, -1500.0)
        p.fix = lambda E: self.fix(E)

        X = numpy.linspace(0, numpy.pi, 100, endpoint=True)
        for i in range(99):
            p.progress()

        pyplot.plot(X, numpy.multiply(numpy.array(p.EV), 0.9))
        pyplot.show()
