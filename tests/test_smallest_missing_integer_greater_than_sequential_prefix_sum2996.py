from problems.smallest_missing_integer_greater_than_sequential_prefix_sum2996 import Solution


def test_example1():
    nums = [1, 2, 3, 2, 5]
    assert Solution().missingInteger(nums) == 6


def test_example2():
    nums = [3, 4, 5, 1, 12, 14, 13]
    assert Solution().missingInteger(nums) == 15


def test_example3():
    nums = [38]
    assert Solution().missingInteger(nums) == 39


def test_example4():
    nums = [46, 8, 2, 4, 1, 4, 10, 2, 4, 10, 2, 5, 7, 3, 1]
    assert Solution().missingInteger(nums) == 47


def test_example5():
    nums = [14, 9, 6, 9, 7, 9, 10, 4, 9, 9, 4, 4]
    assert Solution().missingInteger(nums) == 15
