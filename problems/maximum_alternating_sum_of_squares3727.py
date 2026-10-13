class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=abs)
        ans = 0
        left, right = 0, len(nums) - 1
        take_max = True

        while left <= right:
            if take_max:
                ans += nums[right] ** 2
                right -= 1
            else:
                ans -= nums[left] ** 2
                left += 1
            take_max = not take_max

        return ans
