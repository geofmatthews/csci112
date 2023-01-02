

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fact_unnest(n):
    # call
    if n == 0:
        return_value = 1
        return return_value
    else:
        return_value = fact_unnest(n-1)
        # return
        return_value = n * return_value
        return return_value

def factstack(n):
    stack = [('call', n)]
    while stack != []:
        where, n = stack.pop()
        if where == 'call':
            if n == 0:
                return_value = 1
            else:
                stack.append(('return', n))
                stack.append(('call', n-1))               
        elif where == 'return':
            return_value = n * return_value
    return return_value

for i in range(10):
    print(i, factorial(i), fact_unnest(i), factstack(i))

def pow(a, b):
    if b == 0:
        return 1
    else:
        return a * pow(a, b-1)

def pow_unnest(a, b):
    #call
    if b == 0:
        return_value = 1
        return return_value
    else:
        return_value = pow_unnest(a, b-1)
        # return
        return_value = a * return_value
        return return_value

def powstack(a, b):
    stack = [('call', a, b)]
    while stack != []:
        stack_top = stack.pop()
        where, a, b = stack_top
        if where == 'call':
            if b == 0:
                return_value = 1
            else:
                stack.append(('return', a, b))
                stack.append(('call', a, b-1))
        elif where == 'return':
            return_value = a * return_value
    return return_value

for i in range(10):
    print(i, pow(2,i), pow_unnest(2,i), powstack(2,i))

def powlog(a, b):
    if b == 0:
        return 1
    elif b%2 == 1:
        return a * powlog(a, b-1)
    else:
        return powlog(a, b//2) ** 2

def powlog_unnest(a, b):
    #call
    if b == 0:
        return_value = 1
        return return_value
    elif b%2 == 1:
        return_value = powlog_unnest(a, b-1)
        #return1
        return_value = a * return_value
        return return_value
    else:
        return_value = powlog_unnest(a, b//2)
        # return2
        return_value = return_value ** 2
        return return_value

def powlogstack(a, b):
    stack = [('call', a, b)]
    while stack != []:
        where, a, b = stack.pop()
        if where == 'call':
            if b == 0:
                return_value = 1
            elif b%2 == 1:
                stack.append(('return1', a, b))
                stack.append(('call', a, b-1))
            else:
                stack.append(('return2', a, b))
                stack.append(('call', a, b//2))
        elif where == 'return1':
            return_value = a * return_value
        elif where == 'return2':
            return_value = return_value ** 2
    return return_value

for i in range(10):
    print(i, powlog(2,i), powlog_unnest(2,i), powlogstack(2,i))

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibo_unnest(n):
    # call
    if n < 2:
        return_value = n
        return return_value
    else:
        return_value = fibo_unnest(n-1)
        # return1
        saved_value = return_value
        return_value = fibo_unnest(n-2)
        # return2
        return_value = saved_value + return_value
        return return_value

def fibonaccistack(n):
    stack = [('call', n, 0)]
    while stack != []:
        where, n, saved_value = stack.pop()
        if where == 'call':
            if n < 2:
                return_value = n
            else:
                stack.append(('return1', n, 0))
                stack.append(('call', n-1, 0))
        elif where == 'return1':
            saved_value = return_value
            stack.append(('return2', n, saved_value))
            stack.append(('call', n-2, 0))
        elif where == 'return2':
            return_value = saved_value + return_value
    return return_value

for i in range(10):
    print(i, fibonacci(i), fibo_unnest(i), fibonaccistack(i))
    
def foo(n):
    if n < 2:
        return n
    else:
        return n + foo(n-1) + foo(n-2)
    
def foostack(n):
    stack = [('call', n, 0)]
    while stack != []:
        where, n, saved_value = stack.pop()
        if where == 'call':
            if n < 2:
                return_value = n
            else:
                stack.append(('return1', n, 0))
                stack.append(('call', n-1, 0))
        elif where == 'return1':
            saved_value = return_value
            stack.append(('return2', n, saved_value))
            stack.append(('call', n-2, 0))
        elif where == 'return2':
            return_value = n + saved_value + return_value
    return return_value

for i in range(10):
    print(i, foo(i), foostack(i))
      
            

    
