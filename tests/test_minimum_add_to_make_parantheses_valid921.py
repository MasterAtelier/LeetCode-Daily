from problems.minimum_add_to_make_parantheses_valid921 import Solution


def test_example1():
    s = "())"

    assert Solution().minAddToMakeValid(s) == 1


def test_example2():
    s = "((("

    assert Solution().minAddToMakeValid(s) == 3


def test_single_open_parenthesis():
    s = "("

    assert Solution().minAddToMakeValid(s) == 1


def test_single_close_parenthesis():
    s = ")"

    assert Solution().minAddToMakeValid(s) == 1


def test_already_valid_nested_string():
    s = "((()))()"

    assert Solution().minAddToMakeValid(s) == 0


def test_unmatched_closes_and_opens():
    s = "))(("

    assert Solution().minAddToMakeValid(s) == 4


def test_unmatched_close_between_valid_and_open_parts():
    s = "())("

    assert Solution().minAddToMakeValid(s) == 2


def test_maximum_constraint_length():
    s = "(" * 501 + ")" * 499

    assert Solution().minAddToMakeValid(s) == 2
