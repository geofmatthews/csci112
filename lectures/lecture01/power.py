import time

def powlinear(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

def powlog(a, b):
    def square(x):
        return x*x
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * powlog(a, b-1)
    else:
        return square(powlog(a, b//2))

if __name__ == '__main__':
    print("Test to see if they both work:")
    for i in range(10):
        print(2**i, powlinear(2,i), powlog(2,i))

    print("Speed test:")
    for b in range(22):
        i = 2**b
        print('Computing 2 **', i, 'Linear:', end=' ')
        start = time.process_time_ns()
        x = powlinear(2,i)
        end = time.process_time_ns()
        print((end-start), end=", Log: ")
        start = time.process_time_ns()
        x = powlog(2,i)
        end = time.process_time_ns()
        print((end-start), end=", Native: ")
        start = time.process_time_ns()
        x = 2**i
        end = time.process_time_ns()
        print((end-start))
