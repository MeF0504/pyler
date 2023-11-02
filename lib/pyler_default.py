from pathlib import Path
from datetime import datetime


def time_format(time: float):
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')


def get_size(size_byte: int):
    if size_byte >= 1024**3:
        size = float(size_byte)/1024**3
        pre = 'G'
    elif size_byte >= 1024**2:
        size = float(size_byte)/1024**2
        pre = 'M'
    elif size_byte >= 1024:
        size = float(size_byte)/1024
        pre = 'k'
    else:
        size = size_byte
        pre = ''
    return f'{size:.1f} {pre}B'


def main(item: Path):
    stat = item.stat()
    ret = '''created: {}
last update: {}
file size: {}'''.format(time_format(stat.st_birthtime),
                        time_format(stat.st_mtime),
                        get_size(stat.st_size))
    return ret
