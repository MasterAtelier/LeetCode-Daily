from problems.remove_outermost_parentheses1021 import Solution


def test_example1():
    assert Solution().removeOuterParentheses("(()())(())") == "()()()"


def test_example2():
    assert Solution().removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"


def test_example3():
    assert Solution().removeOuterParentheses("()()") == ""


def test_nested_primitive():
    assert Solution().removeOuterParentheses("((()))") == "(())"


def test_multiple_primitives():
    assert Solution().removeOuterParentheses("()(())") == "()"
