import time

def powlinear (a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

def powlog (a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * powlog (a, b -1)
    else :
        return powlog (a, b //2) ** 2

i = 64
base = 2
while i < 1e7:
    i *= 2
    linstart = time.process_time_ns()
    linresult = powlinear(base,i)
    linend = time.process_time_ns()
    logstart = time.process_time_ns()
    logresult = powlog(base,i)
    logend = time.process_time_ns()
    lintime = linend - linstart
    logtime = logend - logstart
    print(str(i).rjust(10,' '),
          str(lintime).rjust(20,' '),
          str(logtime).rjust(20,' '))
