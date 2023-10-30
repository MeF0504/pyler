import os
import sys
from pathlib import Path
import subprocess

if len(sys.argv) > 1:
    install_path = Path(sys.argv[1])
else:
    if 'XDG_CONFIG_HOME' in os.environ:
        install_path = Path(os.environ['XDG_CONFIG_HOME'])/'pyler'/'src'
    else:
        install_path = Path('~/.config/pyler/src').expanduser()
if install_path.exists():
    print(f'{install_path} already exists.')
    exit()
if not install_path.parent.exists():
    print(f'creating directory {install_path.parent}\n')
    os.mkdir(install_path.parent)

subprocess.run(['git', 'clone', '--recursive',
                'https://github.com/MeF0504/pyler.git', install_path])

if 'PATH' in os.environ \
   and str(install_path/'bin') not in os.environ['PATH'].split(os.pathsep):
    print('\n{}please add {} to your PATH.{}'.format(
        '\033[31m', install_path/'bin', '\033[0m'))
