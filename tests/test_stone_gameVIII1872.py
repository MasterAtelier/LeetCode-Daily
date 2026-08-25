from problems.stone_gameVIII1872 import Solution


def test_example1():

    stones = [-1, 2, -3, 4, -5]

    assert Solution().stoneGameVIII(stones) == 5


def test_example2():

    stones = [7, -6, 5, 10, 5, -2, -6]

    assert Solution().stoneGameVIII(stones) == 13


def test_minimum_input():

    stones = [-10, -12]

    assert Solution().stoneGameVIII(stones) == -22


def test_two_positive_values():

    stones = [1, 2]

    assert Solution().stoneGameVIII(stones) == 3


def test_two_negative_values():

    stones = [-5, -5]

    assert Solution().stoneGameVIII(stones) == -10


def test_zero_values():

    stones = [0, 0]

    assert Solution().stoneGameVIII(stones) == 0


def test_mixed_positive_and_negative_values():

    stones = [1, -1]

    assert Solution().stoneGameVIII(stones) == 0


def test_all_positive_values():

    stones = [5, 5, 5]

    assert Solution().stoneGameVIII(stones) == 15


def test_all_negative_values():

    stones = [-5, -5, -5]

    assert Solution().stoneGameVIII(stones) == 5


def test_longer_sequence():

    stones = [2, -2, 2, -2, 2, -2, 2]

    assert Solution().stoneGameVIII(stones) == 2