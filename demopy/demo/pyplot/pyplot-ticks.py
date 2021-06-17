import numpy
from matplotlib import pyplot

pyplot.figure(1)
X = numpy.linspace(-numpy.pi, numpy.pi, 256, endpoint=True)
C, S = numpy.cos(X), numpy.sin(X)
pyplot.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
pyplot.plot(X, S, color="r", lw=4.0, linestyle="--")

pyplot.xlabel("")
pyplot.legend(loc='upper left')
# axis range
# pyplot.axis('equal')
pyplot.axis([-3.5, 3.5, -1.2, 1.2])
# LaTeX sign
pyplot.xticks([-numpy.pi, -numpy.pi / 2, 0, numpy.pi / 2, numpy.pi],
              [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
pyplot.yticks([-1, 0, +1],
              [r'$-1$', r'$0$', r'$+1$'])

t = 2 * numpy.pi / 3
pyplot.plot()
pyplot.plot([t, t], [0, numpy.cos(t)], color='blue', linewidth=2.5, linestyle="--")
pyplot.scatter([t, ], [numpy.cos(t), ], 50, color='blue')

pyplot.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
                xy=(t, numpy.sin(t)), xycoords='data',
                xytext=(+10, +30), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

pyplot.plot([t, t], [0, numpy.sin(t)], color='red', linewidth=2.5, linestyle="--")
pyplot.scatter([t, ], [numpy.sin(t), ], 50, color='red')

pyplot.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                xy=(t, numpy.cos(t)), xycoords='data',
                xytext=(-90, -50), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", facecolor='purple'))

ax = pyplot.gca()
# remove right,top, and move bottom,left to the center
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
#
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.75))

pyplot.show()
