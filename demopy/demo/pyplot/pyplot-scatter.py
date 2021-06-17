from pylab import *

figure(1)
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)
plot(X, Y + 1, color='blue', alpha=1.00)
plot(X, Y - 1, color='blue', alpha=1.00)

figure(2)
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
scatter(X, Y)

figure(3)
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
    text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
ylim(-1.25, +1.25)

figure(4)


def f(x, y): return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

figure(5)


def f(x, y): return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 10
x = np.linspace(-3, 3, 4 * n)
y = np.linspace(-3, 3, 3 * n)
X, Y = np.meshgrid(x, y)
imshow(f(X, Y))

figure(6)
n = 20
Z = np.random.uniform(0, 1, n)
pie(Z)

figure(7)
n = 8
X, Y = np.mgrid[0:n, 0:n]
quiver(X, Y)

figure(8)
ax = gca()
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)
ax.set_xticklabels([])
ax.set_yticklabels([])

figure(9)
subplot(2, 2, 1)
subplot(2, 2, 3)
subplot(2, 2, 4)

figure(10)
axis([0, 0, 1, 1])
N = 20
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    import random
    from matplotlib.colors import CSS4_COLORS

    co = random.choice(list(CSS4_COLORS.keys()))
    bar.set_facecolor(co)
    bar.set_alpha(0.5)

figure(11)
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

show()
