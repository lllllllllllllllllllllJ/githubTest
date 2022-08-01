# Answer to Question 3
# Converting a decimal to a specified base

# code from https://stackoverflow.com/questions/2088201/integer-to-base-x-system-using-recursion-in-python
# with additions

def _convert(n, base=2):
    # assume remainder is hex (slice off 0x)
    remainder = hex(n%base)[2:]
    if n <= 1:
        # 0, 1 >> end of divisions
        digits = str(n)
    else:
        # concatenate remainders that were left on call stack
        digits = str(_convert(n//base, base)) + str(remainder)
    return digits.lstrip('0')




# Wrapper
def convert(n, base):
    if not isinstance(n, int):
        raise TypeError("Import must be an integer")
    elif n < 0:
        raise TypeError("Function not designed for negatives")
    elif 2 > base > 16:
        raise TypeError("incompatable base")
    else:
        _convert(n, base)



