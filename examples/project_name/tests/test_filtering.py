import unittest


class FilterTests(unittest.TestCase):
    def test_filter_zeros(self):
        self.assertEqual(list(filter(None, [0,1,2]), [1,2]))
