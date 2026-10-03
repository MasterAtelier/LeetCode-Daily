from problems.longest_valid_parantheses32 import Solution


def test_example1():

    s = "(()"

    assert Solution().longestValidParentheses(s) == 2


def test_example2():

    s = ")()())"

    assert Solution().longestValidParentheses(s) == 4


def test_example3_empty_string():

    s = ""

    assert Solution().longestValidParentheses(s) == 0


def test_minimum_nonempty_valid_input():

    s = "()"

    assert Solution().longestValidParentheses(s) == 2


def test_only_unmatched_parentheses():

    s = ")("

    assert Solution().longestValidParentheses(s) == 0


def test_nested_parentheses():

    s = "((()))"

    assert Solution().longestValidParentheses(s) == 6


def test_longest_valid_suffix_after_unmatched_opening():

    s = "((()()"

    assert Solution().longestValidParentheses(s) == 4


def test_maximum_constraint_length():

    s = "(" * 15000 + ")" * 15000

    assert Solution().longestValidParentheses(s) == 30000
