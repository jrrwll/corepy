import numpy
from matplotlib import pyplot

X = numpy.linspace(-numpy.pi, numpy.pi, 256, endpoint=True)
C, S = numpy.cos(X), numpy.sin(X)

pyplot.subplot(211)
pyplot.plot(X, C, color="y", linewidth=2.5, linestyle="-", label="cosine")
pyplot.plot(X, S, color="blue", linewidth=1.5, linestyle="--", label="sine")
pyplot.legend(loc='upper left')

pyplot.subplot(212)
pyplot.plot(X, C, color=(0, 0.75, 0.75), linewidth=2, linestyle="-.", label="cosine")
pyplot.plot(X, S, color="#123456", linewidth=3, linestyle=":", label="sine")
# axis range
pyplot.xlim(-4, 4)
pyplot.ylim(-1.25, 1.25)
pyplot.legend(loc='lower center')

# Get the current Axes instance on the current figure
ax = pyplot.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

pyplot.show()
