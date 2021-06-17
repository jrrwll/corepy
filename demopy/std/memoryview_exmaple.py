from array import array

# signed integer
a = array('h', (i ** 2 for i in range(1, 7)))

mv = memoryview(a)

print('memoryview int ', ', '.join([str(i) for i in mv]))

oct = mv.cast('B')

print('memoryview oct', oct.tolist())
