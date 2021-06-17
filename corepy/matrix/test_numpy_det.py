from unittest import TestCase

import numpy

from corepy.matrix import pascal, hilb


class TestNumpyDet(TestCase):

    def test_logDet(self):
        for i in range(1, 21):
            na = numpy.array(pascal(i))
            print("%d-level det is %f" % (i, numpy.linalg.det(na)))

        for i in range(1, 21):
            na = numpy.array(hilb(i))
            print("%d-level det is %f" % (i, numpy.linalg.det(na)))

        # logdet
        for i in range(1, 21):
            na = numpy.array(pascal(i))
            sign, logDet = numpy.linalg.slogdet(na)
            print("%d-level logDet is %f" % (i, logDet))

        for i in range(1, 21):
            na = numpy.array(hilb(i))
            sign, logDet = numpy.linalg.slogdet(na)
            print("%d-level logDet is %f" % (i, logDet))
