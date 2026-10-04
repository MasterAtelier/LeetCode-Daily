from problems.valid_parenthesis_string678 import Solution


def test_example1():
    s = "()"

    assert Solution().checkValidString(s) is True


def test_example2():
    s = "(*)"

    assert Solution().checkValidString(s) is True


def test_example3():
    s = "(*))"

    assert Solution().checkValidString(s) is True


def test_example4():
    s = "("

    assert Solution().checkValidString(s) is False


def test_single_wildcard_can_be_empty():
    s = "*"

    assert Solution().checkValidString(s) is True


def test_wildcard_cannot_fix_unmatched_open_parentheses():
    s = "*(("

    assert Solution().checkValidString(s) is False


def test_maximum_length_all_wildcards():
    s = "*" * 100

    assert Solution().checkValidString(s) is True


def test_maximum_length_unmatched_open_parentheses():
    s = "(" * 100

    assert Solution().checkValidString(s) is False
