from problems.maximum_alternating_sum_of_squares3727 import Solution


def test_example1():

    nums = [1, 2, 3]

    assert Solution().maxAlternatingSum(nums) == 12


def test_example2_with_negative_values():

    nums = [1, -1, 2, -2, 3, -3]

    assert Solution().maxAlternatingSum(nums) == 16


def test_minimum_input():

    nums = [-7]

    assert Solution().maxAlternatingSum(nums) == 49


def test_duplicate_absolute_values():

    nums = [2, -2, 1, 1]

    assert Solution().maxAlternatingSum(nums) == 6


def test_zero_values():

    nums = [0, -3, 0, 2]

    assert Solution().maxAlternatingSum(nums) == 13


def test_longer_sequence():

    nums = [-5, -4, -3, -2, -1]

    assert Solution().maxAlternatingSum(nums) == 45
