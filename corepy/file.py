import codecs
from pathlib import Path

__boms = (codecs.BOM_UTF8, codecs.BOM_UTF16_BE, codecs.BOM_UTF16_LE,
          codecs.BOM_UTF32_BE, codecs.BOM_UTF32_LE)
__text_chars = bytearray(
    {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})


def is_binary_file(file_path: str) -> bool:
    with open(file_path, 'rb') as f:
        # read 1024 bytes in the head
        chunk = f.read(1024)

        # has utf bom
        header = chunk[0:4]
        if any(header.startswith(bom) for bom in __boms):
            return True

        # check unprintable chars
        if b'\0' in chunk:
            return True

        # unprintable chars threshold
        non_text = sum(byte not in __text_chars for byte in chunk)
        return (non_text / len(chunk)) > 0.3


def load_properties(
        path: str | Path, encoding: str = 'utf-8'
) -> dict[str, str]:
    kvs = {}
    with open(path, encoding=encoding) as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#'):
                continue

            kv = line.split('=', 1)
            if len(kv) != 2 or not kv[0] or not kv[1]:
                continue
            k, v = kv
            kvs[k] = v

    return kvs
