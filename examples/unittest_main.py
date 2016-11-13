import unittest


class Tests(unittest.TestCase):
    # This fails trivially
    def test_foo(self):
        self.assertEqual(1, 2)

# This the idiomatic test for "am I the top-level program" in Python
if __name__ == '__main__':
    # If this is the top-level pmport unittest
    unittest.main()
