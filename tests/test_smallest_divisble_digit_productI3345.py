from problems.smallest_divisible_digit_product_I3345 import Solution

def test_examples1():
    n = 10
    t = 2
    assert Solution().smallestNumber(n, t) == 10

def test_examples2():
    n = 15
    t = 3
    assert Solution().smallestNumber(n, t) == 16

def test_examples3():
    n = 1
    t = 2
    assert Solution().smallestNumber(n, t) == 2

def test_examples4():
    n = 3
    t = 9
    assert Solution().smallestNumber(n, t) == 9

def test_examples5():
    n = 3
    t = 2
    assert Solution().smallestNumber(n, t) == 4