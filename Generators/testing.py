import myfunc
import unittest

class TestMyFunc(unittest.TestCase):
    def testMultiply(self):
        a=3
        b=4
        expected=15
        actual=myfunc.multiply(a,b)
        self.assertEqual(expected, actual, "failed test for 3*4")