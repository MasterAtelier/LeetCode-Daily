from problems.maximum_length_substring_with_two_occurences3090 import Solution


def test_empty_string():
    assert Solution().maximumLengthSubstring("") == 0


def test_single_character():
    assert Solution().maximumLengthSubstring("a") == 1


def test_two_same_characters():
    assert Solution().maximumLengthSubstring("aa") == 2


def test_three_same_characters():
    assert Solution().maximumLengthSubstring("aaa") == 2


def test_all_unique_characters():
    assert Solution().maximumLengthSubstring("abcde") == 5


def test_mixed_characters():
    assert Solution().maximumLengthSubstring("bcbb") == 3


def test_multiple_duplicates():
    assert Solution().maximumLengthSubstring("aabbcc") == 6


def test_requires_shrinking_window():
    assert Solution().maximumLengthSubstring("aaabbb") == 4


def test_longer_example():
    assert Solution().maximumLengthSubstring("aababcabc") == 6


def test_duplicate_at_end():
    assert Solution().maximumLengthSubstring("abcaa") == 4


def test_duplicate_at_start():
    assert Solution().maximumLengthSubstring("aaabc") == 4