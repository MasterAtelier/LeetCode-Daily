from problems.minimum_sum_of_squared_difference2333 import Solution


def test_example1():
    assert Solution().minSumSquareDiff([1, 2, 3, 4, 5], [1, 4, 3, 4, 5], 1, 0) == 1


def test_example2():
    assert Solution().minSumSquareDiff([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 1, 1) == 26


def test_example3():
    assert Solution().minSumSquareDiff([1, 4, 1, 1, 1], [1, 1, 1, 1, 1], 2, 0) == 1


def test_all_differences_can_be_eliminated():
    assert Solution().minSumSquareDiff([1, 10], [4, 2], 20, 0) == 0


def test_zero_operations():
    assert Solution().minSumSquareDiff([1, 8], [5, 2], 0, 0) == 52


def test_leftover_operations_are_distributed_across_equal_differences():
    assert Solution().minSumSquareDiff([5, 5], [0, 0], 2, 0) == 32
