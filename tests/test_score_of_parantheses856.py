from problems.score_of_parantheses856 import Solution


def test_example1():
    s = "()"

    assert Solution().scoreOfParentheses(s) == 1


def test_example2():
    s = "(())"

    assert Solution().scoreOfParentheses(s) == 2


def test_example3():
    s = "()()"

    assert Solution().scoreOfParentheses(s) == 2


def test_nested_groups_add_their_scores():
    s = "(()())"

    assert Solution().scoreOfParentheses(s) == 4


def test_concatenated_nested_groups():
    s = "()(())"

    assert Solution().scoreOfParentheses(s) == 3


def test_deeply_nested_primitive():
    s = "(((())))"

    assert Solution().scoreOfParentheses(s) == 8


def test_maximum_constraint_length():
    s = "(" * 24 + "()" + ")" * 24

    assert Solution().scoreOfParentheses(s) == 1 << 24
