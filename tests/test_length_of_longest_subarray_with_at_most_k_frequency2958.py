from problems.length_of_longest_subarray_with_at_most_k_frequency2958 import Solution


def test_example_1():
    nums = [1, 2, 1, 2, 1, 2, 1, 2]
    k = 2

    assert Solution().maxSubarrayLength(nums, k) == 4


def test_example_2():
    nums = [1, 2, 3, 1, 2, 3, 1, 2]
    k = 2

    assert Solution().maxSubarrayLength(nums, k) == 6


def test_all_elements_unique():
    nums = [1, 2, 3, 4, 5]
    k = 1

    assert Solution().maxSubarrayLength(nums, k) == 5


def test_all_elements_same():
    nums = [1, 1, 1, 1, 1]
    k = 2

    assert Solution().maxSubarrayLength(nums, k) == 2


def test_k_equals_one():
    nums = [1, 2, 3, 1, 2, 3, 4]
    k = 1

    assert Solution().maxSubarrayLength(nums, k) == 4


def test_k_allows_entire_array():
    nums = [1, 1, 2, 2, 3, 3]
    k = 2

    assert Solution().maxSubarrayLength(nums, k) == 6


def test_window_needs_multiple_shrinks():
    nums = [1, 1, 1, 2, 3]
    k = 1

    assert Solution().maxSubarrayLength(nums, k) == 3


def test_duplicate_at_right_boundary():
    nums = [1, 2, 3, 4, 4, 4]
    k = 2

    assert Solution().maxSubarrayLength(nums, k) == 5


def test_longest_window_is_in_middle():
    nums = [1, 1, 2, 3, 4, 2, 2, 5, 5, 5]
    k = 2

    assert Solution().maxSubarrayLength(nums, k) == 6


def test_single_element():
    nums = [7]
    k = 1

    assert Solution().maxSubarrayLength(nums, k) == 1


def test_two_elements_same():
    nums = [5, 5]
    k = 1

    assert Solution().maxSubarrayLength(nums, k) == 1


def test_two_elements_same_k_two():
    nums = [5, 5]
    k = 2

    assert Solution().maxSubarrayLength(nums, k) == 2
