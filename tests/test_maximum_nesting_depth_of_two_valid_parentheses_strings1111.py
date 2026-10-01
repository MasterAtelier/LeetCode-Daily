from problems.maximum_nesting_depth_of_two_valid_parentheses_strings1111 import Solution


def test_example1():
    seq = "(()())"
    assert Solution().maxDepthAfterSplit(seq) == [0, 1, 1, 1, 1, 0]


def test_example2():
    seq = "()(())()"
    assert Solution().maxDepthAfterSplit(seq) == [0, 0, 0, 1, 1, 0, 0, 0]


def test_minimum_input():
    seq = "()"
    assert Solution().maxDepthAfterSplit(seq) == [0, 0]


def test_fully_nested_parentheses():
    seq = "((()))"
    assert Solution().maxDepthAfterSplit(seq) == [0, 1, 0, 0, 1, 0]


def test_concatenated_pairs():
    seq = "()()()"
    assert Solution().maxDepthAfterSplit(seq) == [0, 0, 0, 0, 0, 0]
