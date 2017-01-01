import ast
import importlib
from IPython import get_ipython
from IPython.core.magic import cell_magic, Magics, magics_class
import sys
import unittest
# __file__ = ''


def format_result(result):
    data = []
    details = []
    data.append('FAILURES: {}'.format(len(result.failures)))
    for f in result.failures:
        details.append(('f', f[0]))
    data.append('ERRORS: {}'.format(len(result.errors)))
    for e in result.errors:
        details.append(('e', e[0]))
    data.append('SKIPPED: {}'.format(len(result.skipped)))
    for s in result.skipped:
        details.append(('s', s[0]))
    if result.expectedFailures:
        data.append('EXPECTED FAILURES: {}'.format(
            len(result.expectedFailures)))
        for f in result.expectedFailures:
            details.append(('ef', f[0]))

    if result.unexpectedSuccesses:
        data.append('UNEXPECTED SUCCESSES: {}'.format(
            len(result.unexpectedSuccesses)))
        for s in result.unexpectedSuccesses:
            details.append(('us', s))

    data.append('TOTAL: {}'.format(result.testsRun))

    print(' '.join(data))
    for t, d in details:
        print('{}: {}'.format(t, d))


@magics_class
class UnittestMagics(Magics):
    def __init__(self, shell):
        super(UnittestMagics, self).__init__(shell)
        self.cells = []

    def run_cells(self):
        code = '\n'.join(self.cells)
        node = ast.parse(code, __file__, 'exec')
        mod = importlib.types.ModuleType('__test__')
        for k, v in sys.modules['__main__'].__dict__.items():
            mod.__dict__[k] = v
        exec(compile(node, '__main__', 'exec'), mod.__dict__)
        runner = unittest.defaultTestLoader.loadTestsFromModule(mod)
        result = unittest.TestResult()
        result = runner.run(result)
        format_result(result)

    @cell_magic
    def unittest_reset(self, _, cell):
        self.cells = [cell]

    @cell_magic
    def unittest_append(self, _, cell):
        self.cells.append(cell)

    @cell_magic
    def unittest_complete(self, line, cell):
        self.unittest_append(line, cell)
        self.run_cells()

    @cell_magic
    def unittest_run(self, line, cell):
        self.unittest_reset(line, cell)
        self.run_cells()


get_ipython().register_magics(UnittestMagics)
