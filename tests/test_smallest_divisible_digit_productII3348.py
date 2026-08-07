from problems.smallest_divisible_digit_productII3348 import Solution

def test_example1():
    num = "1234"
    t = 256
    assert Solution().smallestNumber(num, t) == "1488"

def test_example2():
    num = "12355"
    t = 50
    assert Solution().smallestNumber(num, t) == "12355"

def test_example3():
    num = "11111"
    t = 26
    assert Solution().smallestNumber(num, t) == "-1"

def test_example4():
    num = "10"
    t = 320
    assert Solution().smallestNumber(num, t) == "588"