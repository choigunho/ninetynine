import unittest

class TestFunction(unittest.TestCase):

    def test_split(self):
        def split(l, i):
            return l[:i], l[i:]

        self.assertEqual((['a','b','c'],['d','e','f','g','h','i','k']), split(['a','b','c','d','e','f','g','h','i','k'],3))

if __name__ == '__main__':
    unittest.main()