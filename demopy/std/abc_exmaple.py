from collections.abc import *

v = []

# check hashable
isinstance(v, Hashable)

# check callable
callable(v)

# check iterable
# __iter__, or __getitem__, __len__
try:
    it = iter(v)
except TypeError:
    pass

isinstance(v, Iterable) or hasattr(v, '__getitem__')

# check iterator
# __iter__, __next__
isinstance(v, Iterator)
