from problems.generate_parantheses22 import Solution


def test_example1():
    n = 3

    assert Solution().generateParenthesis(n) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]


def test_minimum_input():
    n = 1

    assert Solution().generateParenthesis(n) == ["()"]


def test_two_pairs():
    n = 2

    assert Solution().generateParenthesis(n) == ["(())", "()()"]


def test_zero_pairs():
    n = 0

    assert Solution().generateParenthesis(n) == [""]


def test_maximum_constraint_count_and_validity():
    n = 8
    result = Solution().generateParenthesis(n)

    assert len(result) == 1430
    assert len(set(result)) == 1430
    assert all(len(item) == 2 * n for item in result)
    assert all(is_valid_parentheses(item) for item in result)


def is_valid_parentheses(value: str) -> bool:
    balance = 0
    for char in value:
        balance += 1 if char == "(" else -1
        if balance < 0:
            return False
    return balance == 0
