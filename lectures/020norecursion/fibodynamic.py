

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fibomemo(n, d=None):
    if d is None:
        d = dict()
    if n in d:
        return d[n]
    elif n < 2:
        d[n] = n
        return n
    else:
        result = fibo(n-1) + fibo(n-2)
        d[n] = result
        return result

def fibodynamic(n, d = None):
    if d is None:
        d = [0]*(n+1)
    for i in range(n+1):
        if i < 2:
            d[i] = i
        else:
            d[i] = d[i-1] + d[i-2]
    return d[n]


if __name__ == '__main__':
    for i in range(5,15):
        print(i, fibo(i), fibomemo(i), fibodynamic(i))
