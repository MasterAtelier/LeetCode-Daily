from problems.apply_operations_on_array_to_maximize_sum_of_squares2897 import Solution


def test_example1():
    nums = [2, 6, 5, 8]
    k = 2

    assert Solution().maxSum(nums, k) == 261


def test_example2():
    nums = [4, 5, 4, 7]
    k = 3

    assert Solution().maxSum(nums, k) == 90


def test_single_selected_value_collects_every_available_bit():
    nums = [1, 2, 4]
    k = 1

    assert Solution().maxSum(nums, k) == 49


def test_select_all_values_without_losing_bits():
    nums = [3, 5, 6]
    k = 3

    assert Solution().maxSum(nums, k) == 98


def test_duplicate_values():
    nums = [7, 7, 7, 7]
    k = 2

    assert Solution().maxSum(nums, k) == 98


def test_maximum_value_bits():
    nums = [10**9]
    k = 1

    assert Solution().maxSum(nums, k) == 10**18 % (10**9 + 7)
