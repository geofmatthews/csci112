import string

def parse_token(s):
    if len(s) > 1:
        if s[0] in string.digits + '+-':
            return parse_number(s)
    return s

def parse_number(s):
    try:
        n = int(s)
    except:
        n = float(s)
    return n
    
def tokenize(s):
    return [parse_token(s1) for s1 in s.split()]

