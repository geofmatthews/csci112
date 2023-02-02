import math

def digits(n, base):
    if n == 0:
        return [0]
    rnge = reversed(range(math.ceil(math.log(n,base))))
    return [(n//(base**(i))%(base)) for i in rnge]

def digits2(n, base):
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return list(reversed(result))

cellSize = 5

def just(c, final = False, n=cellSize):
    if final:
        print(c.rjust(n,' '), end='\\\\\n')
    else:
        print(c.rjust(n,' '), end=' & ')
    
def drawLine(digits, n, op=None):
    skip = n - len(digits)
    i = 0
    if op is not None:
        just('$'+op+'$')
        i += 1
        
    while i < n:
        if i < skip:
            just(' ')
        else:
           just(str(digits[i-skip]), i == n-1)
        i += 1
    if op is not None:
        print('\\hline')

def applyOp(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return max(0, a-b)
    elif op == '*':
        return a*b
    
def show(a, b, base, op):
    print('\nBase:', base)
    c = applyOp(a,b,op)
    adigits = digits(a, base)
    bdigits = digits(b, base)
    cdigits = digits(c, base)
    width = max(len(adigits), len(bdigits), len(cdigits)) + 1
    print('\\begin{tabular}{' + 'r'*width + '}')
    drawLine(adigits, width)
    drawLine(bdigits, width, op)
    drawLine(cdigits, width)
    print('\\end{tabular}\n')
##
##show(948, 379, 10, '+')
##show(948, 379, 10, '-')
show(948, 379, 10, '*')
##
##show(2748, 2475, 16, '+')
##show(2748, 685, 16, '-')
show(2748, 685, 16, '*')

show(463, 171, 8, '+')

show(463, 171, 8, '-')
show(463, 171, 8, '*')
