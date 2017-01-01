import ast
import importlib
import ipytest
from IPython import get_ipython
from IPython.core.magic import cell_magic, Magics, magics_class
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)
import sys


@magics_class
class PytestMagics(Magics):
    def __init__(self, shell):
        super(PytestMagics, self).__init__(shell)
        self.cells = []

    def run_cells(self):
        "run tests defined in a cell with pytest"
        ipytest.clean_tests('test_*')
        code = '\n'.join(self.cells)
        node = ast.parse(code, __file__, 'exec')
        mod = importlib.types.ModuleType('__pytest_magics__')
        for k, v in sys.modules['__main__'].__dict__.items():
            mod.__dict__[k] = v
        exec(compile(node, '__pytest_magics__', 'exec'), mod.__dict__)
        ipytest.run_pytest(
            module=mod,
            filename='pytest_magics.py',
            pytest_options=['-q', '--disable-pytest-warnings'])

    @cell_magic
    @magic_arguments()
    @argument('-r', '--reset', action='store_true')
    @argument('-n', '--no-exec', action='store_true')
    def pytest_run(self, arg_string, cell):
        args = parse_argstring(PytestMagics.pytest_run, arg_string)
        if args.reset:
            self.cells = []

        self.cells.append(cell)

        if not args.no_exec:
            self.run_cells()

get_ipython().register_magics(PytestMagics)
