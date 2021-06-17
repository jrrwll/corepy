import functools

try:
    b = 6


    def f1(a):
        print(a)
        print(b)


    def f2(a):
        print(a)
        print(b)
        b = 6


    print(f1(3))
    print(f2(3))
except Exception as e:
    print(type(e), e, '\n')


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print([avg(i) for i in range(1, 11)])

import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        t = time.perf_counter() - t
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            arg_list.append(', '.join(f'{k}={w}' for k, w in sorted(kwargs.items())))

        arg_str = ', '.join(arg_list)
        print(f'[{"%0.8f" % t}] {name}({arg_str}) -> {repr(result)}')

    return clocked
