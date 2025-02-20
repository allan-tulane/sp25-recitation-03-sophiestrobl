from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(5)) == 4*5

def test_quadratic_multiply():
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8