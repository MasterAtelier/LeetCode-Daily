from problems.stone_gameIV1510 import Solution


def test_example1():
    n = 1
    assert Solution().winnerSquareGame(n) is True


def test_example2():
    n = 2
    assert Solution().winnerSquareGame(n) is False


def test_example3():
    n = 4
    assert Solution().winnerSquareGame(n) is True


def test_single_stone():
    n = 1
    assert Solution().winnerSquareGame(n) is True


def test_two_stones():
    n = 2
    assert Solution().winnerSquareGame(n) is False


def test_three_stones():
    n = 3
    assert Solution().winnerSquareGame(n) is True


def test_perfect_square():
    n = 9
    assert Solution().winnerSquareGame(n) is True


def test_known_losing_position():
    n = 7
    assert Solution().winnerSquareGame(n) is False


def test_larger_losing_position():
    n = 17
    assert Solution().winnerSquareGame(n) is False


def test_larger_winning_position():
    n = 18
    assert Solution().winnerSquareGame(n) is True