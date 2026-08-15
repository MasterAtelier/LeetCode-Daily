class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor_all = 0

        for x in nums:
            xor_all ^= x

        if xor_all != 0:
            return len(nums)

        if all(x == 0 for x in nums):
            return 0

        return len(nums) - 1