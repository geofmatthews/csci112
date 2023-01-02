import unittest
from tokens import tokenize

class test_tokenize(unittest.TestCase):
    def test_tokens(self):
        self.assertEqual([123], tokenize('123'))
        self.assertEqual([123, '+', 321], tokenize('123 + 321'))
        self.assertEqual(['(', 123, '+', -321, ')'], tokenize('( 123 + -321 )'))
        self.assertEqual([1e2], tokenize('1e2'))

if __name__ == '__main__':
    unittest.main()
    
