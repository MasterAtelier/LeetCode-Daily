from problems.longest_substring_of_one_repeating_character2213 import Solution


def test_example_1():
    s = "babacc"
    query_characters = "bcb"
    query_indices = [1, 3, 3]

    assert Solution().longestRepeating(s, query_characters, query_indices) == [3, 3, 4]


def test_empty_string():
    s = ""
    query_characters = ""
    query_indices = []

    assert Solution().longestRepeating(s, query_characters, query_indices) == []
