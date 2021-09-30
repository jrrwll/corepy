import numpy
from matplotlib import pyplot

pyplot.figure(1, figsize=(8, 6), dpi=80, frameon=False, clear=True)
# 2 x 2 sub figure, first block
pyplot.subplot(2, 2, 1)
pyplot.plot(numpy.random.beta(numpy.pi, 0.25, 1000))
pyplot.title("figure 2x2-1", color="slateblue")

# 2 x 2 sub figure, second block
pyplot.subplot(212)
pyplot.plot(numpy.random.beta(numpy.pi, 0.75, 1000))
pyplot.title("figure 2x2-2", color="skyblue")

# 2 x 2 sub figure, third block
pyplot.subplot(223)
dt = 0.001
t = numpy.arange(0.0, 10.0, dt)
r = numpy.exp(-t[:1000] / 0.05)
x = numpy.random.randn(len(t))
s = numpy.convolve(x, r)[:len(x)] * dt
pyplot.plot(t, s)
pyplot.axis([0, 1, 1.1 * numpy.amin(s), 2 * numpy.amax(s)])
pyplot.xlabel('time (s)')
pyplot.ylabel('current (nA)')
pyplot.title('Gaussian colored noise')
pyplot.xticks(numpy.linspace(0.0, 1.0, 9, endpoint=True))
pyplot.yticks(numpy.linspace(-0.015, 0.015, 4, endpoint=True))

# save to file
pyplot.savefig("output.png", dpi=144)
# pyplot.close(1)
pyplot.show()
