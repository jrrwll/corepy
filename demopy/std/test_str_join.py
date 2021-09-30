def method1(loop_count):
    out_str = ''
    for num in range(loop_count):
        out_str += repr(num)
    return out_str


# slowest
def method2(loop_count):
    str_list = []
    for num in range(loop_count):
        str_list.append(repr(num))
    return ''.join(str_list)


def method3(loop_count):
    from io import StringIO
    file_str = StringIO()
    for num in range(loop_count):
        file_str.write(repr(num))

    return file_str.getvalue()


# fastest
def method4(loop_count):
    return ''.join([repr(num) for num in range(loop_count)])


def print_cost(loop_count, method_name, method):
    import time
    ts = time.time()
    method(loop_count)
    ts = time.time() - ts
    ts *= 1000
    print("loop %d\t%s cost %.3fms" % (loop_count, method_name, ts))


if __name__ == '__main__':
    methods = [method1, method2, method3, method4]
    for count in [10 ** num for num in range(1, 8)]:
        for i in range(len(methods)):
            print_cost(count, "method%d" % (i + 1), methods[i])
        print()
