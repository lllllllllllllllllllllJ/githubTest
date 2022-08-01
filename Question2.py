# Answer to Q2
# searching online to find an algorthm for the greatest common demonimator through recursion

# code is derived from https://www.tutorialspoint.com/program-to-compute-gcd-of-two-numbers-recursively-in-python
# involves use of a certain 'Euclidian algorthim' ?
# performs poorly with larger inputs incuring more unnececary recursions (creates tree)


def _GCD(n1, n2): 
    denom = 0
    if n1 == n2:
        denom = n1
    elif n2 < 0:
        denom = 1
    elif n1 < n2:
        denom = _GCD(n2, n1) 
    else:
        denom = _GCD(n2, n1 - n2)
    return denom

# wrapper
def GCD(n1, n2):
    if not isinstance(n1, int) and not isinstance(n2, int):
        raise TypeError("Input must be an integer")
    else:
        # allowing use of negatives
        n1, n2 = abs(n1), abs(n2) 
        return _GCD(n1, n2)


