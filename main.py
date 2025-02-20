"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 

    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))


def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)

def pad(x, y):
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y

def quadratic_multiply(x, y):
    return _quadratic_multiply(x, y).decimal_val

def _quadratic_multiply(x, y):
    xvec, yvec = x.binary_vec, y.binary_vec
    xvec, yvec = pad(xvec, yvec)

    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    xL, xR = split_number(xvec)
    yL, yR = split_number(yvec)

    left = _quadratic_multiply(xL, yL)
    right = _quadratic_multiply(xR, yR)
    cross = _quadratic_multiply(xL, yR).decimal_val + _quadratic_multiply(xR, yL).decimal_val

    result = bit_shift(left, len(xvec))
    result = BinaryNumber(result.decimal_val + bit_shift(BinaryNumber(cross), len(xvec) // 2).decimal_val)
    result = BinaryNumber(result.decimal_val + right.decimal_val)

    return result

def test_quadratic_multiply(x, y):
    start = time.time()
    result = quadratic_multiply(BinaryNumber(x), BinaryNumber(y))
    elapsed_time = (time.time() - start) * 1000
    return result, elapsed_time