from problems.stone_gameII1140 import Solution


def test_example1():
    piles = [2, 7, 9, 4, 4]
    assert Solution().stoneGameII(piles) == 10


def test_example2():
    piles = [1, 2, 3, 4, 5, 100]
    assert Solution().stoneGameII(piles) == 104


def test_single_pile():
    piles = [5]
    assert Solution().stoneGameII(piles) == 5


def test_two_piles():
    piles = [1, 2]
    assert Solution().stoneGameII(piles) == 3


def test_equal_piles():
    piles = [1, 1, 1, 1]
    assert Solution().stoneGameII(piles) == 2


def test_large_first_pile():
    piles = [100, 1, 1]
    assert Solution().stoneGameII(piles) == 101


def test_increasing_piles():
    piles = [1, 2, 3, 4, 5]
    assert Solution().stoneGameII(piles) == 8


def test_all_same_large_piles():
    piles = [10, 10, 10, 10, 10, 10]
    assert Solution().stoneGameII(piles) == 30
