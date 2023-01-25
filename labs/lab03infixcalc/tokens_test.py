import unittest
from tokens import tokenize

class test_tokenize(unittest.TestCase):
    def test_tokens(self):
        self.assertEqual([-123], tokenize('-123'))
        self.assertEqual([0.5], tokenize('0.5'))
        self.assertEqual([123, '+', 321], tokenize('123  + 321'))
        self.assertEqual(['(', 123, '+', -321, ')'], tokenize('( 123 + -321 )'))
        self.assertEqual([], tokenize(''))
        self.assertEqual([3], tokenize('3'))
        self.assertEqual([2, '+', 2], tokenize('2 + 2'))
        self.assertEqual([3, '-', -2], tokenize('3 - -2'))
        self.assertEqual(['(', 34, '+', -456.34, ')', '*', '(', '(', 234, '-', 99.4, '**', 2, ')', ')'],
                         tokenize('(    34 + -456.34 ) * ( ( 234 - 99.4 ** 2 ) )'   ))  

if __name__ == '__main__':
    unittest.main()
    
    
