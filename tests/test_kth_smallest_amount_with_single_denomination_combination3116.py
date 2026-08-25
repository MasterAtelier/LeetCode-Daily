from problems.kth_smallest_amount_with_single_denomination_combination3116 import Solution


def test_example1():

    coins = [3, 6, 9]
    k = 3

    assert Solution().findKthSmallest(coins, k) == 9


def test_example2():

    coins = [5, 2]
    k = 7

    assert Solution().findKthSmallest(coins, k) == 12


def test_minimum_input():

    coins = [1]
    k = 1

    assert Solution().findKthSmallest(coins, k) == 1


def test_single_denomination():

    coins = [25]
    k = 4

    assert Solution().findKthSmallest(coins, k) == 100


def test_overlapping_multiples():

    coins = [2, 3, 5]
    k = 10

    assert Solution().findKthSmallest(coins, k) == 14


def test_large_k():

    coins = [1]
    k = 2_000_000_000

    assert Solution().findKthSmallest(coins, k) == 2_000_000_000