# Answer to Q5
# implementation of towers of Hanoi


def _moveDisk(n, src, dest, spaces):
    print(spaces + "Recursion level is %d" % (len(spaces)/4)) 
    print(spaces + "moving disc %d from %d to %d" % (n, src, dest))
    print(spaces + "n = %d, src = %d, dest = %d\n" % (n, src, dest))


def _towers(n, src, dest, spaces):
    spaces += "    "
    if n == 1:
        _moveDisk(n, src, dest, spaces)
    else:
        tmp = 6 - src - dest
        _towers(n - 1, src, tmp, spaces)
        _moveDisk(n, src, dest, spaces)
        _towers(n - 1, tmp, dest, spaces)


# Wrapper
def towers(n, src, dest, spaces=""):
            ...

if __name__ == "__main__":

    towers(2, 1, 2)