'''
Created on Sep 30, 2013

@author: leen
'''
import unittest
import random
from negabinary.negabinary import *

class GeneralNegabinaryTest(unittest.TestCase):

    def testConvert(self):
        for _ in xrange(10000):
            a = random.randint(0, 2**31)
            b = random.randint(-2**31, 0)
            A = get_negabinary_from_decimal(a)
            B = get_negabinary_from_decimal(b)
            self.assertEqual(a, get_decimal_from_negabinary(A))
            self.assertEqual(b, get_decimal_from_negabinary(B))
    def testAdd(self):
        for _ in xrange(10000):
            a = random.randint(0, 2**31)
            b = random.randint(-2**31, 0)
            A = get_negabinary_from_decimal(a)
            B = get_negabinary_from_decimal(b)
            c = a + b
            C = add_two_negabinary(A, B)
            self.assertEqual(c, get_decimal_from_negabinary(C))

if __name__ == "__main__":
    unittest.main()