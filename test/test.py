'''
Created on Sep 30, 2013

@author: leen
'''
import unittest
import random
from negabinary.negabinary import *

class GeneralNegabinaryTest(unittest.TestCase):

    """def testConvert(self):
        for _ in xrange(10000):
            a = random.randint(-2**31, 2**31)
            b = random.randint(-2**31, 2**31)
            A = get_negabinary_from_decimal(a)
            B = get_negabinary_from_decimal(b)
            self.assertEqual(a, get_decimal_from_negabinary(A))
            self.assertEqual(b, get_decimal_from_negabinary(B))"""
    def testWiki(self):
        a = 85
        b = 52
        A = get_negabinary_from_decimal(a)
        B = get_negabinary_from_decimal(b)
        C = add_two_negabinary(A, B)
        cc = get_decimal_from_negabinary(C)
        self.assertEqual(a+b, cc , str(a)+ " "+str(b)+ " "+ str(a+b)+ " "+str(cc) )

    def testAdd(self):
        for _ in xrange(100000):
            a = random.randint(-2**31, 2**31)
            b = random.randint(-2**31, 2**31)
            A = get_negabinary_from_decimal(a)
            B = get_negabinary_from_decimal(b)
            c = a + b
            C = add_two_negabinary(A, B)
            cc = get_decimal_from_negabinary(C)
            self.assertEqual(c, cc , str(a)+ " "+str(b)+ " "+ str(c)+ " "+str(cc) )

if __name__ == "__main__":
    unittest.main()