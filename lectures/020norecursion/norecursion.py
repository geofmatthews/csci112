def push(s, item):
    s.append(item)
def pop(s):
    return s.pop()
def stack():
    return list()
def empty(s):
    return s == []

def mypow(n, p):
    if p == 0:
        return 1
    elif p % 2 == 1:
        return n * mypow(n, p-1)
    else:
        return mypow(n, p//2) ** 2

# conceptual recursion elimination:
# only have to remember whether to multiply
# by n or square:
def mypowstack(n, p):
    s = stack()
    while p > 0:
        if p % 2 == 1:
            push(s, 'multiply')
            p -= 1
        else:
            push(s, 'square')
            p //= 2
    accumulator = 1
    while not(empty(s)):
        if s.pop() == 'multiply':
            accumulator *= n
        else:
            accumulator *= accumulator
    return accumulator
            
# Eliminate recursion syntactically:   
# step 1, eliminate nested recursion:
def mypow1(n, p):
    if p == 0:
        return 1
    elif p % 2 == 1:
        returnval = mypow1(n, p-1)
        return n * returnval
    else:
        returnval = mypow1(n, p//2)
        return returnval**2

# step 2, add location markers at start and after all recursive calls:
def mypow2(n, p):
    # location A
    if p == 0:
        return 1
    elif p % 2 == 1:
        returnval = mypow2(n, p-1)
        # location B
        return n * returnval
    else:
        returnval = mypow2(n, p//2)
        # location C
        return returnval**2

# step 3, eliminate recursion with push and pop:
#      stack location and local vars needed after recursion
#      for recurive calls stack a call to the continuation
#        UNDERNEATH the call to the start of the function
#      to use the return of a function call use returnval
#      to return something just assign it to returnval
def mypow3(n, p):
    s = stack()
    push(s, ['A', [n, p]])
    while not(empty(s)):
        location, vars = pop(s)
        if location == 'A':
            n,p = vars
            if p == 0:
                returnval = 1
            elif p % 2 == 1:
                push(s, ['B', [n]])
                push(s, ['A', [n, p-1]])
            else:
                push(s, ['C', []])
                push(s, ['A', [n, p//2]])
        elif location == 'B':
            n = vars[0]
            returnval = n * returnval
        elif location == 'C':
            returnval = returnval**2
    return returnval

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fibo1(n):
    if n < 2:
        return n
    else:
        returnval1 = fibo1(n-1)
        returnval2 = fibo1(n-2)
        return returnval1 + returnval2

def fibo2(n):
    # location A
    if n < 2:
        return n
    else:
        returnval1 = fibo2(n-1)
        # location B
        returnval = fibo2(n-2)
        # location C
        return returnval1 + returnval

def fibo3(n):
    s = stack()
    push(s, ['A', [n]])
    while not(empty(s)):
        location, vars = s.pop()
        if location == 'A':
            n = vars[0]
            if n < 2:
                returnval = n
            else:
                push(s, ['B', [n]])
                push(s, ['A', [n-1]])
        elif location == 'B':
            n = vars[0]
            push(s, ['C', [returnval]])
            push(s, ['A', [n-2]])
        elif location == 'C':
            returnval1 = vars[0]
            returnval = returnval1 + returnval
    return returnval

def even(n):
    if n == 0:
        return True
    else:
        return not(odd(n-1))
def odd(n):
    if n == 0:
        return False
    else:
        return not(even(n-1)) 

if __name__ == '__main__':
    for i in range(5,12):
        print(pow(2,i), mypowstack(2,i), mypow(2,i), mypow1(2,i), mypow2(2,i), mypow3(2,i))
        print(fibo(i), fibo1(i), fibo2(i), fibo3(i))

                
