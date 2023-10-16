#! /usr/bin/env python3

import sys
from pathlib import Path
import mimetypes
from importlib import import_module

_lib_root = Path(__file__).parent.parent/'lib'
sys.path.append(str(_lib_root))
import pyler_default


def main():
    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        print(f'file {file_path} does not exist')

    mtype, _ = mimetypes.guess_type(file_path.name)
    if mtype is None:
        lib = pyler_default
    else:
        # info = mtype
        lib_path1 = _lib_root/f'{mtype}.py'  # sub type lib
        lib_path2 = lib_path1.parent/'__init__.py'  # type lib
        if lib_path1.is_file():
            lib = import_module(mtype.replace('/', '.'))
        elif lib_path2.is_file():
            lib = import_module(lib_path2.parent.name)
        else:
            lib = pyler_default
    print('=== start ===')
    print(lib.main(file_path))
    print('=== end ===')


if __name__ == '__main__':
    main()
