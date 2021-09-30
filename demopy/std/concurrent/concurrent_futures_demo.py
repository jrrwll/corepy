import collections
import random
import time
from concurrent import futures
from enum import Enum

executor = futures.ThreadPoolExecutor(max_workers=4)
results = executor.map(lambda x: x ** x, range(1, 10))
print(time.strftime(f'[%H:%M:%S] {list(results)}'))


class Status(Enum):
    ok = 1
    error = 2


def download_one():
    time.sleep(random.random())


def download_many(task_count, worker_count=None):
    counter = collections.Counter()
    with futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
        to_do_map = {}
        for i in range(task_count):
            future = executor.submit(download_one)
            to_do_map[future] = i

        done_iter = futures.as_completed(to_do_map)
        for future in done_iter:
            try:
                res = future.result()
            except Exception as e:
                error_msg = 'Error'
                status = Status.error
            else:
                error_msg = ''
                status = Status.ok

            counter[status] += 1
            if error_msg:
                i = to_do_map[future]
                print('*** Error for {}: {}'.format(i, error_msg))
    return counter


task_count = 32
worker_count = 8
t0 = time.time()
counter = download_many(task_count=task_count, worker_count=worker_count)
assert sum(counter.values()) == task_count, \
    'some downloads are unaccounted for'
elapsed = time.time() - t0
print('-' * 20)
msg = '{} flag{} downloaded.'
plural = 's' if counter[Status.ok] != 1 else ''
print(msg.format(counter[Status.ok], plural))
if counter[Status.error]:
    plural = 's' if counter[Status.error] != 1 else ''
    print('{} error{}.'.format(counter[Status.error], plural))
print('elapsed time: {:.2f}s'.format(elapsed))
