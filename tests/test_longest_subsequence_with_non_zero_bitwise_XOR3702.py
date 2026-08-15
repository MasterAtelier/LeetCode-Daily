
import pytest

from problems.longest_subsequence_with_non_zero_bitwise_XOR3702 import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Official-style examples
        ([1, 2, 3], 2),
        ([2, 3, 4], 3),

        # Single element
        ([0], 0),
        ([1], 1),
        ([100], 1),

        # All zeros
        ([0, 0], 0),
        ([0, 0, 0], 0),
        ([0, 0, 0, 0, 0], 0),

        # Total XOR = 0, but non-zero values exist
        ([1, 1], 1),
        ([1, 2, 3], 2),
        ([1, 1, 1, 1], 3),
        ([0, 1, 1], 2),
        ([0, 0, 1, 1], 3),
        ([5, 5], 1),

        # Total XOR != 0
        ([1, 2], 2),
        ([1, 3], 2),
        ([2, 3, 4], 3),
        ([0, 1], 2),
        ([0, 0, 5], 3),
        ([7, 7, 1], 3),

        # Larger repeated values
        ([1] * 5, 5),
        ([1] * 6, 5),
        ([2, 2, 2], 3),
        ([2, 2, 2, 2], 3),

        # Mixed values
        ([0, 2, 2, 4], 4),
        ([0, 3, 5, 6], 3),
    ],
)
def test_longest_subsequence(solution, nums, expected):
    assert solution.longestSubsequence(nums) == expected


def test_does_not_modify_input(solution):
    nums = [1, 2, 3, 4]
    original = nums.copy()

    solution.longestSubsequence(nums)

    assert nums == original


def test_large_all_zero_input(solution):
    nums = [0] * 100_000

    assert solution.longestSubsequence(nums) == 0


def test_large_non_zero_xor_input(solution):
    nums = [1] * 100_000

    # 100000 copies of 1 -> even count -> XOR is 0.
    # At least one non-zero element exists, so answer is n - 1.
    assert solution.longestSubsequence(nums) == 99_999


def test_large_input_with_non_zero_total_xor(solution):
    nums = [1] * 99_999

    # Odd count of 1 -> XOR is 1.
    assert solution.longestSubsequence(nums) == 99_999


def test_property_when_total_xor_is_zero_and_non_zero_exists(solution):
    test_cases = [
        [1, 1],
        [2, 2],
        [3, 3],
        [1, 2, 3],
        [4, 4, 7, 7],
        [0, 1, 1],
        [0, 0, 2, 2],
    ]

    for nums in test_cases:
        xor_all = 0

        for x in nums:
            xor_all ^= x

        assert xor_all == 0
        assert any(x != 0 for x in nums)

        assert solution.longestSubsequence(nums) == len(nums) - 1