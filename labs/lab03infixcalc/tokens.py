'''
Tokenizes infix arithmetric expressions.
converts ints and floats (but not sci notation: 1e5)
symbols: + = * / ^
and parentheses left as strings
Uses split() so all tokens must be separated by spaces.

Geoffrey Matthews
2023
'''

import string, re

def parse_number(s):
    try:
        return int(s)
    except:
        try:
           return float(s)
        except:
            return s

def tokenize(s):
    return [parse_number(x) for x in s.split()]

if __name__ == '__main__':
    s1 = '(   34 + 456.34 ) * ( ( 234 - 99.4 ** 2) )'
    print(tokenize(s1))
    print(tokenize('2 - -2'))
