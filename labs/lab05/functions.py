
def func01(n):
    if n < 2:
        return 3*n
    else:
        return 2*func01(n-1)

for n in range(10):
    print(func01(n), end=' ')
print()

def func02(n):
    if n < 2:
        return 3*n
    elif n < 6:
        return n*n
    else:
        return 3 + 2*func02(n-2)

for n in range(10):
    print(func02(n), end=' ')
print()
    

def func03(n):
    if n < 2:
        return 3*n
    else:
        return 3*func03(n-1) + 2*func03(n-2)

for n in range(10):
    print(func03(n), end=' ')
print()
    


def func04(n):
    if n < 2:
        return 3*n
    elif n%2 == 1:
        return 7 + func04(n - 3)
    else:
        return func04(n-1) * 2*func04(n//2)

for n in range(10):
    print(func04(n), end=' ')
print()
    

def func05(a, b):
    if a == 0:
        return b+3
    elif b == 0:
        return a*2
    else:
        return 2*a + 3*b + 4*func05(a-1,b) + 5*func05(a, b-1)


for a in range(5):
    for b in range(5):
        print(func05(a, b), end=' ')
    print()
print()
    
