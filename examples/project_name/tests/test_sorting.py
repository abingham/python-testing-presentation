import unittest


class SortingTests(unittest.TestCase):
    def test_basic(self):
        self.assertListEqual(sorted([3, 2, 1]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
