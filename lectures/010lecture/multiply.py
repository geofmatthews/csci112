

def classic_multiply(a, b):
    bdigits = reversed([int(x) for x in list(str(b))])
    sum = 0
    for i, digit in enumerate(bdigits):
        sum += digit*a*10**i
    return sum

print(classic_multiply(347, 182))

def peasant_multiply(a, b):
    sum = 0
    while b > 0:
        print(a,b)
        if b%2 == 1:
            sum += a
        a,b = a*2, b//2
    return sum

print(peasant_multiply(347,182))



def fibonacci(n):
  a,b = 0,1
  while n > 0:
    n,a,b = n-1, b, a+b
  return a

for i in range(10):
    print(fibonacci(i))
