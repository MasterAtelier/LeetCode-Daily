from collections import Counter
class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0] + 1

        counter = Counter(nums)
        seq_sum = nums[0]
        
        for i in range(1, len(nums) ):
            if nums[i] != nums[i - 1] + 1:
                break
            seq_sum += nums[i]

        while seq_sum in counter:
            seq_sum += 1
        return seq_sum