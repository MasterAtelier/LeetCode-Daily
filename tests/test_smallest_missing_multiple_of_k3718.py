from problems.smallest_missing_multiple_of_k3718 import Solution


def test_example1():

    nums = [8, 2, 3, 4, 6]
    k = 2

    assert Solution().missingMultiple(nums, k) == 10


def test_example2():

    nums = [1, 4, 7, 10, 15]
    k = 5

    assert Solution().missingMultiple(nums, k) == 5


def test_first_multiple_missing():

    nums = [1, 2, 3, 4]
    k = 5

    assert Solution().missingMultiple(nums, k) == 5


def test_minimum_input():

    nums = [1]
    k = 1

    assert Solution().missingMultiple(nums, k) == 2


def test_single_element_not_multiple():

    nums = [1]
    k = 100

    assert Solution().missingMultiple(nums, k) == 100


def test_consecutive_multiples():

    nums = [3, 6, 9, 12, 15]
    k = 3

    assert Solution().missingMultiple(nums, k) == 18


def test_gap_between_multiples():

    nums = [4, 8, 16, 20]
    k = 4

    assert Solution().missingMultiple(nums, k) == 12


def test_non_multiples_mixed_with_multiples():

    nums = [1, 2, 3, 5, 6, 7, 9, 10, 12]
    k = 3

    assert Solution().missingMultiple(nums, k) == 15


def test_k_equal_to_maximum_constraint():

    nums = [100]
    k = 100

    assert Solution().missingMultiple(nums, k) == 200


def test_longer_sequence():

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    k = 1

    assert Solution().missingMultiple(nums, k) == 16