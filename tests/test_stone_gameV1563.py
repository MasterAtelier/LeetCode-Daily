from problems.stone_gameV1563 import Solution


def test_example1():

    stoneValue = [6, 2, 3, 4, 5, 5]

    assert Solution().stoneGameV(stoneValue) == 18


def test_example2():

    stoneValue = [7, 7, 7, 7, 7, 7, 7]

    assert Solution().stoneGameV(stoneValue) == 28


def test_example3():

    stoneValue = [4]

    assert Solution().stoneGameV(stoneValue) == 0


def test_example4():

    stoneValue = [1, 2]

    assert Solution().stoneGameV(stoneValue) == 1


def test_example5():

    stoneValue = [1, 2, 3]

    assert Solution().stoneGameV(stoneValue) == 4


def test_example6():

    stoneValue = [1, 1, 1, 1]

    assert Solution().stoneGameV(stoneValue) == 3


def test_example7():

    stoneValue = [10, 1, 1]

    assert Solution().stoneGameV(stoneValue) == 3


def test_example8():

    stoneValue = [1, 10, 1]

    assert Solution().stoneGameV(stoneValue) == 1