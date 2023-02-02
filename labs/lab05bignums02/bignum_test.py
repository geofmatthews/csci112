from bignum import Bignum

import unittest, random

class BignumTests(unittest.TestCase):
    def testInt(self):
        self.assertEqual(Bignum(0), Bignum(0))
        self.assertEqual(Bignum(1234), Bignum(1234))
        self.assertEqual(Bignum(1234).int(), 1234)
        self.assertEqual(Bignum(-1234).int(), -1234)
        self.assertEqual(Bignum(2**100).int(), 2**100)
        self.assertEqual(Bignum(2**1000,100).int(), 2**1000)

    def testAdd(self):
        b1 = Bignum(123)
        b2 = Bignum(321)
        b3 = Bignum(444)
        self.assertEqual(b1.add(b2), b3)
        b4 = Bignum(-123)
        self.assertEqual(b1.add(b2), b4.add(b2))

    def testSub(self):
        b1 = Bignum(333)
        b2 = Bignum(222)
        b3 = Bignum(111)
        self.assertEqual(b1.sub(b2), b3)
        b11 = Bignum(333333)
        b12 = Bignum(333)
        b13 = Bignum(333000)
        self.assertEqual(b11.sub(b12), b13)
        self.assertEqual(b12.sub(b11), Bignum(-333000))
        self.assertEqual(b11.sub(b11), Bignum(0))
        b15 = Bignum(-333)
        self.assertEqual(b15.sub(b11), b12.sub(b11))
        self.assertEqual(Bignum(-1).sub(Bignum(-111)), Bignum(-110))

    def testCmp(self):
        b1 = Bignum(111)
        b2 = Bignum(222)
        b3 = Bignum(333333)
        b4 = Bignum(444444)
        b5 = Bignum(-111)
        b6 = Bignum(-1111)
        self.assertEqual(b1.cmp(b2), -1)
        self.assertEqual(b1.cmp(b1), 0)
        self.assertEqual(b1.cmp(b3), -1)
        self.assertEqual(b3.cmp(b1), 1)
        self.assertEqual(b4.cmp(b3), 1)
        self.assertEqual(b5.cmp(b6), -1)
        self.assertEqual(b1.cmp(b5), 0)

    def testLessThan(self):
        b1 = Bignum(111)
        b2 = Bignum(-111)
        b3 = Bignum(111111)
        b4 = Bignum(-111111)
        self.assertTrue(b2 < b1)
        self.assertFalse(b1 < b2)
        self.assertTrue(b2 < b3)
        self.assertTrue(b4 < b3)
        self.assertTrue(b4 < Bignum(0))
        self.assertFalse(b3 < Bignum(0))
        self.assertTrue(Bignum(0) < b1)
        self.assertFalse(Bignum(0) < b2)
        self.assertFalse(b1 < b1)
        
    def testPlus(self):
        b1 = Bignum(111)
        b2 = Bignum(-111)
        b3 = Bignum(111111)
        b4 = Bignum(-111111)
        self.assertEqual(b1 + b2, Bignum(0))
        self.assertEqual(b3 + b4, Bignum(0))
        self.assertEqual(b1 + b4, Bignum(-111000))
        self.assertEqual(b2 + b3, Bignum(111000))

    def testMinus(self):
        b1 = Bignum(111)
        b2 = Bignum(-111)
        b3 = Bignum(111111)
        b4 = Bignum(-111111)
        self.assertEqual(b3 - b3, Bignum(0))
        self.assertEqual(b1 - b2, Bignum(222))
        self.assertEqual(b2 - b1, Bignum(-222))
        self.assertEqual(b3 - b1, Bignum(111000))
        self.assertEqual(b3 - b2, Bignum(111222))
        self.assertEqual(b4 - b1, Bignum(-111222))
        self.assertEqual(b4 - b2, Bignum(-111000))
        self.assertEqual(b4 - b2, Bignum(-111000))
        self.assertEqual(b2 - b4, Bignum(111000))

    def testMiscellaneous(self):
        for base in [2, 17, 1033, 98473]:
            for i in range(1000):
                i1 = random.randint(-1_000_000_000, 1_000_000_000)
                i2 = random.randint(-1_000_000_000, 1_000_000_000)
                self.assertEqual(i1+i2,
                                 (Bignum(i1,base) + Bignum(i2,base)).int())
                self.assertEqual(i1 - i2,
                                 (Bignum(i1,base) - Bignum(i2,base)).int())
                

if __name__ == '__main__':
    unittest.main(verbosity = 2)
