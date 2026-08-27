from problems.lexicographically_smallest_permutation_greater_than_target3720 import Solution


def test_example1():

    s = "abc"
    target = "bba"

    assert Solution().lexGreaterPermutation(s, target) == "bca"


def test_example2():

    s = "leet"
    target = "code"

    assert Solution().lexGreaterPermutation(s, target) == "eelt"


def test_example3():

    s = "baba"
    target = "bbaa"

    assert Solution().lexGreaterPermutation(s, target) == ""


def test_minimum_input():

    s = "a"
    target = "a"

    assert Solution().lexGreaterPermutation(s, target) == ""


def test_single_character_greater():

    s = "b"
    target = "a"

    assert Solution().lexGreaterPermutation(s, target) == "b"


def test_target_smaller_than_smallest_permutation():

    s = "abc"
    target = "aaa"

    assert Solution().lexGreaterPermutation(s, target) == "abc"


def test_target_is_exact_permutation():

    s = "abc"
    target = "abc"

    assert Solution().lexGreaterPermutation(s, target) == "acb"


def test_target_is_largest_permutation():

    s = "abc"
    target = "cba"

    assert Solution().lexGreaterPermutation(s, target) == ""


def test_duplicate_characters():

    s = "aabc"
    target = "aacb"

    assert Solution().lexGreaterPermutation(s, target) == "abac"


def test_all_characters_same():

    s = "aaaa"
    target = "aaaa"

    assert Solution().lexGreaterPermutation(s, target) == ""


def test_backtracking_required():

    s = "aabb"
    target = "abba"

    assert Solution().lexGreaterPermutation(s, target) == "baab"


def test_greater_at_last_position():

    s = "aabc"
    target = "aabb"

    assert Solution().lexGreaterPermutation(s, target) == "aabc"


def test_longer_representative_input():

    s = "aabbcc"
    target = "abccab"

    assert Solution().lexGreaterPermutation(s, target) == "abccba"