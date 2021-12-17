import importlib
from pip._internal import main as pipmain
import shlex


def install_import(package, version):
    try:
        return importlib.import_module(package)
    except ModuleNotFoundError:
        cmd = shlex.split(f'install -U {package}{version}')
        print(cmd)
        pipmain(cmd)
    return importlib.import_module(package)
