from problems.removing_minimum_and_maximum_from_array2091 import Solution


def test_example1():

    nums = [2, 10, 7, 5, 4, 1, 8, 6]

    assert Solution().minimumDeletions(nums) == 5


def test_example2():

    nums = [0, -4, 19, 1, 8, -2, -1, 5]

    assert Solution().minimumDeletions(nums) == 3


def test_example3():

    nums = [101]

    assert Solution().minimumDeletions(nums) == 1


def test_minimum_input():

    nums = [1, 2]

    assert Solution().minimumDeletions(nums) == 2


def test_minimum_and_maximum_at_opposite_ends():

    nums = [1, 2, 3, 4, 5]

    assert Solution().minimumDeletions(nums) == 2


def test_both_removed_from_left():

    nums = [1, 5, 3, 4, 2]

    assert Solution().minimumDeletions(nums) == 2


def test_both_removed_from_right():

    nums = [5, 3, 4, 2, 1]

    assert Solution().minimumDeletions(nums) == 2


def test_remove_from_both_ends():

    nums = [2, 10, 7, 5, 4, 1, 8, 6]

    assert Solution().minimumDeletions(nums) == 5


def test_minimum_before_maximum():

    nums = [1, 3, 4, 5, 2]

    assert Solution().minimumDeletions(nums) == 3


def test_maximum_before_minimum():

    nums = [5, 3, 4, 2, 1]

    assert Solution().minimumDeletions(nums) == 2


def test_duplicate_values():

    nums = [2, 1, 3, 3, 1, 2]

    assert Solution().minimumDeletions(nums) == 3


def test_negative_values():

    nums = [-10, -5, -3, -8, -1]

    assert Solution().minimumDeletions(nums) == 2


def test_longer_sequence():

    nums = [7, 4, 9, 2, 6, 3, 8, 1, 5, 10, 11, 0]

    assert Solution().minimumDeletions(nums) == 2