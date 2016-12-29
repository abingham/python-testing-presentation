import ast
import importlib
import ipytest
from IPython.core.magic import register_cell_magic
import sys


@register_cell_magic
def pytest_run(_, cell):
    "run tests defined in a cell with pytest"
    ipytest.clean_tests('test_*')
    node = ast.parse(cell, __file__, 'exec')
    mod = importlib.types.ModuleType('__test__')
    for k, v in sys.modules['__main__'].__dict__.items():
        mod.__dict__[k] = v
    exec(compile(node, '__test__', 'exec'), mod.__dict__)
    ipytest.run_pytest(module=mod, pytest_options=['-q'])
