import random

def digits(n, base):
    if n == 0:
        return [0]
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return list(reversed(result))

def putcell(item, final=False):
    if final:
        ending = '\\\\\n'
    else:
        ending = ' &'
    print(item, end=ending)

def putdigits(nums, width, op=None):
    if op is not None:
        putcell('$'+op+'$')
        width -= 1
    for i in range(width - len(nums)):
        putcell(' ')
    for i in range(len(nums)):
        putcell(str(nums[i]), i == len(nums)-1)
    if op is not None:
        print('\\hline')

def applyop(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

def putop(a, b, op, base):
    c = applyop(a,b,op)
    adigits = digits(a,base)
    bdigits = digits(b,base)
    cdigits = digits(c,base)
    width = max(len(adigits),len(bdigits),len(cdigits)) + 1
    print('\\begin{tabular}{' + 'r'*width + '}')
    putdigits(adigits, width)
    putdigits(bdigits, width, op)
    putdigits(cdigits, width)
    print('\\end{tabular}\\hfill')
    print()

n1 = random.randint(1000,9999)
n2 = random.randint(1000,9999)
if n1 < n2:
    n1,n2 = n2,n1

putop(n1, n2, '+', 10)
putop(n1, n2, '-', 10)
putop(n1, n2, '+', 8)
putop(n1, n2, '-', 8)
putop(n1, n2, '+', 16)
putop(n1, n2, '-', 16)
    
    
    
