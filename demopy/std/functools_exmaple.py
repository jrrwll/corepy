from functools import reduce, partial
from operator import mul, itemgetter


def fact(n):
    return reduce(mul, range(1, n + 1))


print(', '.join([str(callable(o)) for o in (1, str, fact, hash)]))

data = [('a', 3), ('b', 2), ('c', 1)]
for i in sorted(data, key=itemgetter(1)):
    print(i)

import unicodedata

nfc = partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print((s1, s2))
print(s1 == s2)
print((nfc(s1), nfc(s2)))
print(nfc(s1) == nfc(s2))
