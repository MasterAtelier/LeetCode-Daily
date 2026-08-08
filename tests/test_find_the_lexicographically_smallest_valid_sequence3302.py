from problems.find_the_lexicographically_smallest_valid_sequence3302 import Solution

def test_basic_example_1():
    word1 = "vbcca"
    word2 = "abc"
    expected = [0, 1, 2]
    assert Solution().validSequence(word1, word2) == expected

def test_basic_example_2():
    word1 = "bacdc"
    word2 = "abc"
    expected = [1, 2, 4]
    assert Solution().validSequence(word1, word2) == expected


def test_exact_match():
    word1 = "abc"
    word2 = "abc"
    expected = [0, 1, 2]
    assert Solution().validSequence(word1, word2) == expected

def test_mismatch_at_beginning():
    word1 = "xbc"
    word2 = "abc"
    expected = [0, 1, 2]
    assert Solution().validSequence(word1, word2) == expected

def test_mismatch_in_middle():
    word1 = "axc"
    word2 = "abc"
    expected = [0, 1, 2]
    assert Solution().validSequence(word1, word2) == expected

def test_mismatch_at_end():
    word1 = "abx"
    word2 = "abc"
    expected = [0, 1, 2]
    assert Solution().validSequence(word1, word2) == expected


def test_repeated_characters():
    word1 = "aaaa"
    word2 = "aaa"
    expected = [0, 1, 2]
    assert Solution().validSequence(word1, word2) == expected

def test_repeated_characters_with_mismatch():
    word1 = "aaac"
    word2 = "aaa"
    expected = [0, 1, 2]
    assert Solution().validSequence(word1, word2) == expected

def test_more_than_one_mismatch():
    word1 = "aaa"
    word2 = "abc"
    expected = []
    assert Solution().validSequence(word1, word2) == expected

def test_word2_longer_than_word1():
    word1 = "ab"
    word2 = "abc"
    expected = []
    assert Solution().validSequence(word1, word2) == expected


def test_single_character_mismatch():
    word1 = "abc"
    word2 = "x"
    expected = [0]
    assert Solution().validSequence(word1, word2) == expected

def test_empty_word1():
    word1 = ""
    word2 = "a"
    expected = []
    assert Solution().validSequence(word1, word2) == expected

def test_empty_word2():
    word1 = "abc"
    word2 = ""
    expected = []
    assert Solution().validSequence(word1, word2) == expected
