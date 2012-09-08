import unittest

class TestFunction(unittest.TestCase):

    def test(self):
        def slice(l, i, j):
            return l[i-1:j]

        self.assertEqual((['c','d','e','f','g']), slice(['a','b','c','d','e','f','g','h','i','k'],3,7))

if __name__ == '__main__':
    unittest.main()