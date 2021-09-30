import matplotlib.colors
import matplotlib.lines
import numpy
from matplotlib import pyplot

for k, v in matplotlib.colors.BASE_COLORS.items():
    print(f"'{k}'\t'{v}'")

for k, v in matplotlib.colors.CSS4_COLORS.items():
    print(f"'{k}'\t'{v}'")

for name, hex in matplotlib.colors.cnames.items():
    print(f"'{name}'\t'{hex}'")

for name, hex in matplotlib.lines.lineMarkers.items():
    print(f"'{name}'\t'{hex}'")

for name, hex in matplotlib.lines.lineStyles.items():
    print(f"'{name}'\t'{hex}'")

print(f"{', '.join(matplotlib.lines.fillStyles)}")

x = numpy.arange(0.0, 5.0, 0.2)
# red dashes, blue squares and green triangles
pyplot.plot(
    # red solid
    x, x, 'r-',
    # cyan broken
    x, numpy.sqrt(x), 'c--',
    # magenta square
    x, numpy.cos(x), 'ms',
    # black triangle
    x, numpy.log1p(x), 'k^',
    # yellow
    x, x ** 2 / 2, 'yD',
    x, numpy.arctan(x), 'g.',

)
pyplot.show()
