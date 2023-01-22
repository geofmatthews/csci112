import unittest
from tokens import tokenize

class test_tokenize(unittest.TestCase):
    def test_tokens(self):
        self.assertEqual([1e10], tokenize('1e10'))
        self.assertEqual([-123], tokenize('-123'))
        self.assertEqual([0.5], tokenize('.5'))
        self.assertEqual([123, '+', 321], tokenize('123  + 321'))
        self.assertEqual(['(', 123, '+', -321, ')'], tokenize('(123+-321)'))
        self.assertEqual([1e2], tokenize('1e2'))
        self.assertEqual([], tokenize(''))
        self.assertEqual([3], tokenize('3'))
        self.assertEqual([3, '-', -2], tokenize('3--2'))
        self.assertEqual([33, '**', 44], tokenize('33**44'))
                         

if __name__ == '__main__':
    unittest.main()
    
