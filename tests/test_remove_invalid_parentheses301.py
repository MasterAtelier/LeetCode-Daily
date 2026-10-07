from problems.remove_invalid_parantheses301 import Solution


def test_example1():
    s = "()())()"

    assert set(Solution().removeInvalidParentheses(s)) == {"(())()", "()()()"}


def test_example2():
    s = "(a)())()"

    assert set(Solution().removeInvalidParentheses(s)) == {"(a())()", "(a)()()"}


def test_example3():
    s = ")("

    assert set(Solution().removeInvalidParentheses(s)) == {""}


def test_already_valid_string_is_unchanged():
    s = "(ab)c"

    assert Solution().removeInvalidParentheses(s) == [s]


def test_letters_are_preserved_when_all_parentheses_are_removed():
    s = "a)b(c"

    assert set(Solution().removeInvalidParentheses(s)) == {"abc"}


def test_repeated_parentheses_do_not_create_duplicate_results():
    s = "((("

    assert Solution().removeInvalidParentheses(s) == [""]


def test_twenty_identical_parentheses_boundary():
    s = ")" * 20

    assert Solution().removeInvalidParentheses(s) == [""]
