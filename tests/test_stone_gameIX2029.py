import pytest

from problems.stone_gameIX2029 import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "stones, expected",
    [
        ([2, 1], True),
        ([2, 1, 3], False),
        ([5, 1, 2, 4, 3], False),
        ([1], False),
        ([2], False),
        ([3], False),
        ([1, 2], True),
        ([1, 1], False),
        ([2, 2], False),
        ([3, 3], False),
        ([1, 2, 3], False),
        ([1, 1, 1, 2], True),
        ([1, 1, 1, 1, 2], True),
        ([1, 1, 1, 1, 1, 2], True),
        ([1, 1, 1, 1, 1, 1, 2], True),
    ],
)
def test_stone_game_ix(solution, stones, expected):
    assert solution.stoneGameIX(stones) is expected


def test_all_stones_are_divisible_by_three(solution):
    assert solution.stoneGameIX([3, 6, 9, 12]) is False
    assert solution.stoneGameIX([3, 6, 9]) is False


def test_even_zero_residue_count_requires_both_nonzero_residues(solution):
    assert solution.stoneGameIX([3, 6, 1]) is False
    assert solution.stoneGameIX([3, 6, 2]) is False
    assert solution.stoneGameIX([3, 6, 1, 2]) is True


def test_odd_zero_residue_count_uses_difference_condition(solution):
    assert solution.stoneGameIX([3, 1, 2]) is False
    assert solution.stoneGameIX([3, 1, 1, 2]) is False
    assert solution.stoneGameIX([3, 1, 1, 1, 2]) is False


def test_values_only_their_remainder_matters(solution):
    assert solution.stoneGameIX([1, 4, 7, 2, 5, 8]) == solution.stoneGameIX(
        [1, 1, 1, 2, 2, 2]
    )


def test_large_input(solution):
    stones = [1] * 100000
    assert solution.stoneGameIX(stones) is False


def test_large_input_with_balanced_residues(solution):
    stones = [1] * 50000 + [2] * 50000
    assert solution.stoneGameIX(stones) is True