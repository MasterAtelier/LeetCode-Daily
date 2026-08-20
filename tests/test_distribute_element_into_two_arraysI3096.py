from problems.distribute_element_into_two_arraysI3096 import Solution


def test_example1():
    nums = [2, 1, 3]
    assert Solution().resultArray(nums) == [2, 3, 1]


def test_example2():
    nums = [5, 4, 3, 8]
    assert Solution().resultArray(nums) == [5, 3, 4, 8]


def test_minimum_input():
    nums = [1, 2]
    assert Solution().resultArray(nums) == [1, 2]


def test_equal_values_go_to_arr2():
    nums = [1, 1, 1, 1]
    assert Solution().resultArray(nums) == [1, 1, 1, 1]


def test_all_elements_go_to_arr1_after_initialization():
    nums = [10, 1, 9, 8, 7]
    assert Solution().resultArray(nums) == [10, 9, 8, 7, 1]


def test_all_elements_go_to_arr2_after_initialization():
    nums = [1, 10, 9, 8, 7]
    assert Solution().resultArray(nums) == [1, 10, 9, 8, 7]


def test_negative_values():
    nums = [-1, -5, -2, -3]
    assert Solution().resultArray(nums) == [-1, -2, -3, -5]


def test_duplicate_values():
    nums = [3, 2, 3, 2, 3]
    assert Solution().resultArray(nums) == [3, 3, 2 , 2, 3]


def test_longer_sequence():
    nums = [2, 1, 3, 4, 5, 6]
    assert Solution().resultArray(nums) == [2, 3, 4, 5, 6, 1]