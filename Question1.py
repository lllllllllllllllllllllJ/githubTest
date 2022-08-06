# Answer to Q1 (with additions from Q4)
# implementing recursive and iterative solutions for Fibinacci / Factorial

# ==== Functions ==== #

def _factorialIterative(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact

def _factorialRec(n):
    fact = 1
    if n > 1:
        fact = n * _factorialRec(n - 1)
    return fact

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

def _fibinacciRec(n):
    fib = 0
    if n < 2:
        fib = n
    else:
        fib = _fibinacciRec(n - 1) + _fibinacciRec(n - 2)
    return fib

# ===== Wrappers ===== # Redundant ? Can i use control flags ?

def factorialIterative(n): 
    if not isinstance(n, int):
        raise TypeError("Import must be an integer")
    elif n < 0:
        raise ValueError("Import must not be negative")
    else:
        return _factorialIterative(n)

def factorialRec(n): 
    if not isinstance(n, int):
        raise TypeError("Import must be an integer")
    elif n < 0:
        raise ValueError("Import must not be negative")
    else:
        return _factorialRec(n)


def fibinacciIterative(n): 
    if not isinstance(n, int):
        raise TypeError("Import must be an integer")
    elif n < 0:
        raise ValueError("Import must not be negative")
    else:
        return _fibinacciIterative(n)


def fibinacciRec(n): 
    if not isinstance(n, int):
        raise TypeError("Import must be an integer")
    elif n < 0:
        raise ValueError("Import must not be negative")
    else:
        return _fibinacciRec(n) 

# Declare stackoverflow error and add to Recursive functions

    
