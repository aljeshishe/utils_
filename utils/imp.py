import importlib
import os
import types

from pip._internal import main as pipmain
import shlex

print('imp')


def reload(package):
    assert(hasattr(package, "__package__"))
    fn = package.__file__
    fn_dir = os.path.dirname(fn) + os.sep
    module_visit = {fn}
    del fn

    def reload_recursive_ex(module):
        try:
            importlib.reload(module)
        except ModuleNotFoundError as e:  # if submodule removed avoid dexception: spec not found for the module 'utils.common'
            print(f'{e.__class__.__name__}: {e}')

        for module_child in vars(module).values():
            if isinstance(module_child, types.ModuleType):
                fn_child = getattr(module_child, "__file__", None)
                if (fn_child is not None) and fn_child.startswith(fn_dir):
                    if fn_child not in module_visit:
                        # print("reloading:", fn_child, "from", module)
                        module_visit.add(fn_child)
                        reload_recursive_ex(module_child)

    return reload_recursive_ex(package)


def install_import(package, version=''):
    try:
        return importlib.import_module(package)
    except ModuleNotFoundError:
        cmd = shlex.split(f'install -U {package}{version}')
        print(cmd)
        pipmain(cmd)
    return importlib.import_module(package)
