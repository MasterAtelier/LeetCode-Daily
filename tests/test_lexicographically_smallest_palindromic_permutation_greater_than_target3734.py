from problems.lexicographically_smallest_palindromic_permutation_greater_than_target3734 import Solution


def test_example1():

    s = "babab"
    target = "abbab"

    assert Solution().lexPalindromicPermutation(s, target) == "abbba"


def test_example2_no_palindromic_permutation():

    s = "abc"
    target = "aaa"

    assert Solution().lexPalindromicPermutation(s, target) == ""


def test_minimum_input_equal_target():

    s = "a"
    target = "a"

    assert Solution().lexPalindromicPermutation(s, target) == ""


def test_single_character_greater_than_target():

    s = "b"
    target = "a"

    assert Solution().lexPalindromicPermutation(s, target) == "b"


def test_all_identical_characters():

    s = "aaaa"
    target = "aaaa"

    assert Solution().lexPalindromicPermutation(s, target) == ""


def test_even_length_palindrome():

    s = "aabb"
    target = "abba"

    assert Solution().lexPalindromicPermutation(s, target) == "baab"


def test_odd_length_palindrome_with_backtracking():

    s = "aabbc"
    target = "abcba"

    assert Solution().lexPalindromicPermutation(s, target) == "bacab"


def test_target_smaller_than_smallest_palindrome():

    s = "aabb"
    target = "aaaa"

    assert Solution().lexPalindromicPermutation(s, target) == "abba"


def test_target_greater_than_all_palindromic_permutations():

    s = "aabb"
    target = "bbaa"

    assert Solution().lexPalindromicPermutation(s, target) == ""


def test_duplicate_characters():

    s = "aaabbb"

    target = "ababab"

    assert Solution().lexPalindromicPermutation(s, target) == ""


def test_multiple_odd_frequencies():

    s = "aabc"
    target = "aaaa"

    assert Solution().lexPalindromicPermutation(s, target) == ""


def test_longer_representative_input():

    s = "aabbccddeeff"
    target = "abcddcbaefef"

    assert Solution().lexPalindromicPermutation(s, target) == "abcdeffedcba"
