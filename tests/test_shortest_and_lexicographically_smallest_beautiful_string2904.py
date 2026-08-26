from problems.shortest_and_lexicographically_smallest_beautiful_string2904 import Solution


def test_example1():

    s = "100011001"

    k = 3

    assert Solution().shortestBeautifulSubstring(s, k) == "11001"


def test_example2():

    s = "1011"

    k = 2

    assert Solution().shortestBeautifulSubstring(s, k) == "11"


def test_example3():

    s = "000"

    k = 1

    assert Solution().shortestBeautifulSubstring(s, k) == ""


def test_minimum_input():

    s = "1"

    k = 1

    assert Solution().shortestBeautifulSubstring(s, k) == "1"


def test_no_beautiful_substring():

    s = "0000"

    k = 1

    assert Solution().shortestBeautifulSubstring(s, k) == ""


def test_single_one_with_leading_zeroes():

    s = "0001000"

    k = 1

    assert Solution().shortestBeautifulSubstring(s, k) == "1"


def test_all_ones():

    s = "111111"

    k = 3

    assert Solution().shortestBeautifulSubstring(s, k) == "111"


def test_exactly_k_ones_in_entire_string():

    s = "101001"

    k = 3

    assert Solution().shortestBeautifulSubstring(s, k) == "101001"


def test_lexicographically_smallest_equal_length_candidate():

    s = "1011101"

    k = 2

    assert Solution().shortestBeautifulSubstring(s, k) == "11"


def test_leading_zeroes_are_removed():

    s = "0001011000"

    k = 2

    assert Solution().shortestBeautifulSubstring(s, k) == "11"


def test_longer_sequence():

    s = "0010010110010101"

    k = 3

    assert Solution().shortestBeautifulSubstring(s, k) == "1011"
