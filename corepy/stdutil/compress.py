import bz2
import contextlib
import gzip
import os
import tarfile
import zipfile
import zlib

'''
bz2, gzip, zlib
'''


def zlib_it(data, level=5, mode='zlib'):
    if mode.lower() == 'zlib' or mode.lower() == 'z':
        cps = zlib_it().compressobj(level)
        return cps.compress(data)
    elif mode.lower() == 'gzip' or mode.lower() == 'gz':
        return gzip.compress(data, compresslevel=level)
    elif mode.lower() == 'bzip2' or mode.lower() == 'bz2':
        return bz2.compress(data, compresslevel=level)
    else:
        raise ValueError('The arg "mode" must in ["z", "gz", "bz2"]')


def unzlib_it(data, mode='zlib'):
    if mode.lower() == 'zlib' or mode.lower() == 'z':
        return zlib.decompress(data)
    elif mode.lower() == 'gzip' or mode.lower() == 'gz':
        return gzip.decompress(data)
    elif mode.lower() == 'bzip2' or mode.lower() == 'bz2':
        return bz2.decompress(data)
    else:
        raise ValueError('The arg "mode" must in ["z", "gz", "bz2"]')


# ZIP_STORED、ZIP_DEFLATED、ZIP_BZIP2、ZIP_LZMA
# allowZip64=True to big data
def zip_text(text, target, level=zipfile.ZIP_DEFLATED, allowZip64=False, add=False, textName='README', ):
    mode = 'a' if add else 'w'
    with zipfile.ZipFile(target, mode, compression=level, allowZip64=allowZip64) as z:
        z.writestr(textName, text)


def zip_files(filenames, target, level=zipfile.ZIP_DEFLATED, allowZip64=False, add=False):
    mode = 'a' if add else 'w'
    with zipfile.ZipFile(target, mode, compression=level, allowZip64=allowZip64) as z:
        if type(filenames) is str:
            z.write(filenames)
            return

        for filename in filenames:
            if os.path.isdir(filename):
                zip_dir(filename, target, compression=level, allowZip64=allowZip64, add=True)
            else:
                z.write(filename)


def zip_dir(dirname, target, level=zipfile.ZIP_DEFLATED, allowZip64=False, add=False):
    mode = 'a' if add else 'w'
    filelist = []
    for par, dirs, files in os.walk(dirname):
        for file in files:
            filelist.append(os.path.join(par, file))

    with zipfile.ZipFile(target, mode, compression=level, allowZip64=allowZip64) as z:
        for tar in filelist:
            # 在压缩包中的 相对路径
            arcname = tar[len(dirname):]
            z.write(tar, arcname)


def unzip(source, dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname, 0o777)
    with zipfile.ZipFile(source, 'r') as z:
        for name in z.namelist():
            name = name.replace('\\', '/')

            if name.endswith('/'):
                os.mkdir(os.path.join(dirname, name))
            else:
                ext_filename = os.path.join(dirname, name)
                ext_dir = os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir, 0o777)
                with open(ext_filename, 'wb') as f:
                    f.write(z.read(name))


# mode in ['w', 'w:gz', 'w:bz2', 'w:xz', 'a'}
def tar_files(filenames, target, mode='w'):
    with contextlib.closing(tarfile.open(target, mode)) as t:
        if type(filenames) is str:
            t.add(filenames)
            return

        for filename in filenames:
            if os.path.isdir(filename):
                tar_dir(filename, target, 'a')
            else:
                t.add(filename)


def tar_dir(dirname, target, mode='w'):
    filelist = []
    for par, dirs, files in os.walk(dirname):
        for file in files:
            filelist.append(os.path.join(par, file))

    with contextlib.closing(tarfile.open(target, mode)) as t:
        for tar in filelist:
            arcname = tar[len(dirname):]
            t.add(tar, arcname)


def untar(source, dirname):
    with contextlib.closing(tarfile.open(source, 'r:*')) as t:
        t.extractall(dirname)


_DEFAULT_COMPRESS_LEVEL = 9


# bzip2
def bzip2_text(text, target, level=_DEFAULT_COMPRESS_LEVEL):
    with contextlib.closing(bz2.BZ2File(target, 'w', level)) as b:
        b.write(text)


def bzip2_tar(tarname, dirname, level=_DEFAULT_COMPRESS_LEVEL):
    data = None
    arcname = None
    if '/' in tarname:
        arcname = tarname[(tarname.rindex('/')) + 1:] + '.bz2'
    else:
        arcname = tarname + '.bz2'
    if dirname[-1] != '/':
        arcname = dirname + '/' + arcname
    else:
        arcname = dirname + arcname

    with open(tarname, 'rb') as f:
        data = f.read()
    with contextlib.closing(bz2.BZ2File(arcname, 'w', level)) as b:
        b.write(data)


def unbzip2(source, dirname, text=False):
    data = None
    with contextlib.closing(bz2.BZ2File(source, 'r')) as b:
        data = b.read()
        if text:
            return data

    if '/' in source:
        arcname = source[(source.rindex('/')) + 1:]
    else:
        arcname = source

    if arcname[-4:].upper() == '.BZ2':
        arcname = arcname[:-4]

    if dirname[-1] != '/':
        arcname = dirname + '/' + arcname
    else:
        arcname = dirname + arcname

    with open(arcname, 'wb') as f:
        f.write(data)


def gzip_text(text, target, level=_DEFAULT_COMPRESS_LEVEL):
    with gzip.open(target, 'wb', level) as g:
        g.write(text)


def gzip_tar(tarname, dirname, level=_DEFAULT_COMPRESS_LEVEL):
    data = None
    arcname = None
    if '/' in tarname:
        arcname = tarname[(tarname.rindex('/')) + 1:] + '.gz'
    else:
        arcname = tarname + '.gz'
    if dirname[-1] != '/':
        arcname = dirname + '/' + arcname
    else:
        arcname = dirname + arcname

    with open(tarname, 'rb') as f:
        data = f.read()
    with gzip.open(arcname, 'w', level) as b:
        b.write(data)


def ungzip(source, dirname, text=False):
    data = None
    with gzip.open(source, 'r') as b:
        data = b.read()
        if text:
            return data

    if '/' in source:
        arcname = source[(source.rindex('/')) + 1:]
    else:
        arcname = source

    if arcname[-3:].upper() == '.GZ':
        arcname = arcname[:-3]

    if dirname[-1] != '/':
        arcname = dirname + '/' + arcname
    else:
        arcname = dirname + arcname

    with open(arcname, 'wb') as f:
        f.write(data)
