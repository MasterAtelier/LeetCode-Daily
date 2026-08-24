import pytest

from problems.sum_game1927 import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "num, expected",
    [
        # No question marks: sums are already unequal, so Alice wins.
        ("1234", True),

        # No question marks: sums are equal, so Alice loses.
        ("1221", False),

        # Odd number of question marks -> Alice wins.
        ("??5?", True),

        # Two question marks can be balanced by Bob.
        ("??", False),

        # Equal number of question marks and equal known sums.
        ("?1?1", False),

        # Two question marks, but the known sums are not equal.
        ("?2?1", True),

        # Question marks are imbalanced between halves and exactly compensate.
        ("?0009?", True),

        # Same setup but known difference cannot be compensated.
        ("?0008?", True),

        # All question marks with an even count.
        ("????", False),

        # All question marks with an odd count.
        ("???", True),

        # Single character is not a valid LeetCode input, included only
        # to keep the test suite focused on the problem constraints.
    ],
)
def test_sum_game(solution, num, expected):
    assert solution.sumGame(num) is expected


def test_sum_game_known_example(solution):
    assert solution.sumGame("5023") is False


def test_sum_game_large_balanced_case(solution):
    num = "?" * 100
    assert solution.sumGame(num) is False


def test_sum_game_large_odd_question_count(solution):
    num = "?" * 101
    assert solution.sumGame(num) is True
