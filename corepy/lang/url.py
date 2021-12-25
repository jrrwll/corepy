import timeit
import urllib.request


def wget(urls, target_dir='', min_size=0):
    if type(urls) is str:
        _wget(urls, target_dir, min_size)
    else:
        for url in urls:
            _wget(url, target_dir, min_size)


def _wget(url, target_dir, min_size):
    after_slash = url[url.rindex('/') + 1:]
    filename = after_slash[after_slash.index('?') + 1:] \
        if '?' in after_slash else after_slash

    target_file = filename
    if target_dir:
        if target_dir[-1] != '/':
            target_dir += '/'
        target_file = target_dir + filename

    data = urllib.request.urlopen(url).read()
    size = len(data)
    with open(target_file, 'wb') as file:
        if size >= min_size:
            file.write(data)

    return size


def time_wget(url, target_dir='', min_size=0):
    print("Download file from " + url + " ...")

    dt = timeit.timeit()
    size = _wget(url, target_dir, min_size)
    dt = timeit.timeit() - dt

    print("The file size: " + str(size / 1024) + " KB")
    print("The spent time: " + str(dt) + " s")
    print("The download speed: " + str(size / 1024 / dt) + " KB/s")
