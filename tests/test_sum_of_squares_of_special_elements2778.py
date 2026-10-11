from problems.sum_of_squares_of_special_elements2778 import Solution


def test_example1():
    nums = [1, 2, 3, 4]

    assert Solution().sumOfSquares(nums) == 21


def test_example2():
    nums = [2, 7, 1, 19, 18, 3]

    assert Solution().sumOfSquares(nums) == 63


def test_minimum_input():
    nums = [7]

    assert Solution().sumOfSquares(nums) == 49


def test_duplicate_values():
    nums = [5, 5, 5, 5]

    assert Solution().sumOfSquares(nums) == 75


def test_special_indices_at_one_and_length():
    nums = [3, 8, 6]

    assert Solution().sumOfSquares(nums) == 45
