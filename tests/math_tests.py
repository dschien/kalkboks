from kalkboks.math import cagr

__author__ = 'schien'

import unittest


class MyTestCase(unittest.TestCase):

    def test_growth(self):
        i_0 = 1
        alpha = 0.50
        t = 2
        i = cagr(i_0, alpha, t)
        self.assertEqual(i, 2.25)


if __name__ == '__main__':
    unittest.main()
