import bisect
import random

FMT = '{0:.2f} @ {1:2d}    {2}{0:<.2f}'

n = random.random()
r = [random.random() for i in range(9)]
r.append(n)
bisect.insort(r, n)
r = sorted(r)

c = [i * 0.1 for i in range(10)]
c.append(n)
c.sort()

print('random -->  ', ' '.join('%.2f' % i for i in r))
for i in reversed(c):
    # see bisect.bisect_left
    pos = bisect.bisect(r, i)
    offset = pos * '    |'
    print(FMT.format(i, pos, offset))

print('const  -->  ', ' '.join('%.2f' % i for i in c))
