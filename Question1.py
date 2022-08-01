# Answer to Q1 (with additions from Q4)
# implementing recursive and iterative solutions for Fibinacci / Factorial


def calcNFactorial(n, type='r'): # am i aloud to use a control flag here ?
    if not isinstance(n, int):
        raise TypeError("Import must be an integer")
    elif n < 0:
        raise ValueError("Import must not be negative")
    else:
        return _factorialRec(n)


# iterative
def _factorialIterative(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact

# recursive
def _factorialRec(n):
    fact = 1
    if n > 1:
        fact = n * _factorialRec(n - 1)
    return fact

# iterative 
def _fibinacciIterative(n):
    fib = 0
    current = 1
    prev = 0
    if n < 2:
        first = n 
    else:
        for i in range(2, n + 1):
            fib = current + prev
            prev = current
            current = fib
    return fib 

# Recursive
def _fibinacciRec(n):
    fib = 0
    if n < 2:
        fib = n
    else:
        fib = _fibinacciRec(n - 1) + _fibinacciRec(n - 2)
    return fib


# just for checking
if __name__ == "__main__": 
    try:
        print(calcNFactorial("er"))
    except ValueError as e:
        print("invalid argument: ", e)

    
    
