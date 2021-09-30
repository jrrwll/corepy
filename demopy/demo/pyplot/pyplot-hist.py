import numpy
from matplotlib import pyplot

pyplot.figure(1)
mu, sigma = 100, 15
x = mu + sigma * numpy.random.randn(10000)
n, bins, patches = pyplot.hist(x, 50, density=1, facecolor='pink', alpha=0.75)
pyplot.xlabel('Smarts')
pyplot.ylabel('Probability')
pyplot.title('Histogram of IQ')
pyplot.text(60, .025, r'$\mu=100,\ \sigma=15$')
# [left, bottom, width, height]
pyplot.axis(rect=[40, 160, 0, 0.03], axisbg='w')
pyplot.grid(True)
