'''
Tokenizes infix arithmetric expressions.
converts ints and floats
symbols: + = * / **
and parentheses left as strings

Geoffrey Matthews
2023
'''

import string

def parse_number(s):
    try:
        n = int(s)
    except:
        try:
            n = float(s)
        except:
            return s
    return n

def split_string(s):
    if len(s) == 0:
        return []
    elif s[0] in string.whitespace:
        return split_string(s[1:])
    elif s[0] in '()+/':
        return [s[0]] + split_string(s[1:])
    elif s[0] == '*':
        if s[1] == '*':
            return [s[0:2]] + split_string(s[2:])
        else:
            return [s[0]] + split_string(s[1:])
    elif s[0] == '-':
        if s[1] not in string.digits:
            return [s[0]] + split_string(s[1:])
    toke = ''
    if s[0] in '+-':
        toke += s[0]
        s = s[1:]
    while s and s[0] in string.digits:
        toke += s[0]
        s = s[1:]
    if s and s[0] in '.':
        toke += s[0]
        s = s[1:]
    while s and s[0] in string.digits:
        toke += s[0]
        s = s[1:]
    if s and s[0] in 'e':
        toke += s[0]
        s = s[1:]
    while s and s[0] in string.digits:
        toke += s[0]
        s = s[1:]
    return [toke] + split_string(s)
    
def tokenize(s):
    return [parse_number(s1) for s1 in split_string(s)]

