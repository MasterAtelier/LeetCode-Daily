class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for index, value in enumerate(nums):
            if n % (index + 1) == 0:
                total += value * value

        return total
