from problems.make_lexicographically_smallest_array_by_swapping_elements2948 import Solution


def test_example1():

    nums = [1, 5, 3, 9, 8]
    limit = 2

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 3, 5, 8, 9]


def test_example2():

    nums = [1, 7, 6, 18, 2, 1]
    limit = 3

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 6, 7, 18, 1, 2]


def test_example3():

    nums = [1, 7, 28, 19, 10]
    limit = 3

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 7, 28, 19, 10]


def test_minimum_input():

    nums = [1]
    limit = 1

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1]


def test_all_elements_in_one_group():

    nums = [5, 1, 3, 2, 4]
    limit = 4

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 2, 3, 4, 5]


def test_no_swaps_possible():

    nums = [1, 10, 20, 30]
    limit = 1

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 10, 20, 30]


def test_transitive_grouping():

    nums = [5, 1, 3]
    limit = 2

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 3, 5]


def test_duplicate_values():

    nums = [4, 2, 4, 3, 2]
    limit = 2

    assert Solution().lexicographicallySmallestArray(nums, limit) == [2, 2, 3, 4, 4]


def test_boundary_difference_equal_to_limit():

    nums = [5, 1, 3]
    limit = 2

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 3, 5]


def test_multiple_independent_groups():

    nums = [8, 1, 5, 10, 3, 12]
    limit = 2

    assert Solution().lexicographicallySmallestArray(nums, limit) == [8, 1, 3, 10, 5, 12]


def test_longer_sequence():

    nums = [10, 4, 7, 2, 8, 15, 14, 20, 19, 1]
    limit = 3

    assert Solution().lexicographicallySmallestArray(nums, limit) == [1, 2, 4, 7, 8, 14, 15, 19, 20, 10]