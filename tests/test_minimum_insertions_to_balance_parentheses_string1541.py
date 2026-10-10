from problems.minimum_insertions_to_balance_parentheses_string1541 import Solution


def test_example1():
    assert Solution().minInsertions("(()))") == 1


def test_example2():
    assert Solution().minInsertions("())") == 0


def test_example3():
    assert Solution().minInsertions("))())(") == 3


def test_single_open_parenthesis():
    assert Solution().minInsertions("(") == 2


def test_single_close_parenthesis():
    assert Solution().minInsertions(")") == 2


def test_open_after_odd_close_requirement():
    assert Solution().minInsertions("(()(") == 5
