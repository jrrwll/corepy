import itertools

gen = itertools.count(1, 5)
print(next(gen), next(gen), next(gen))

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, 5))
print(list(gen))

gen = itertools.combinations(range(5), 3)
print(list(gen))


def concat_iter(*iters):
    for it in iters:
        yield from it


gen = concat_iter('abc', range(3))
print(list(gen))


def simple_coro(a):
    print(f'started: a = {a}')
    b = yield a
    print(f'received: b = {b}')
    c = yield a + b
    print(f'received: c = {c}')


mycoro = simple_coro(13)
from inspect import getgeneratorstate

print(getgeneratorstate(mycoro))
# or next(mycoro)
print(f'return: {mycoro.send(None)}')
print(getgeneratorstate(mycoro))
print(f'return: {mycoro.send(25)}')
print(getgeneratorstate(mycoro))
try:
    print(f'return: {mycoro.send(76)}')
finally:
    print(getgeneratorstate(mycoro))
    mycoro.close()

import functools


def cotoutine(func):
    @functools.wraps(func)
    def primer(*arg, **kwargs):
        gen = func(*arg, **kwargs)
        next(gen)
        return gen

    return primer


from collections import namedtuple


@cotoutine
def averager():
    total = 0
    count = 0
    avg = None
    while True:
        term = yield avg
        if term is None:
            break

        total += term
        count += 1
        avg = total / count
    # as a value of StopIteration
    # expect StopIteration as e, then e.value is set
    return namedtuple('Averager', 'Count')(avg, count)
