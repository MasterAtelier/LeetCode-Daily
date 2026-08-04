class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        ans = []
        st = set(nums)
        lower_bound = min(nums)
        upper_bound = max(nums)
        for i in range(lower_bound, upper_bound):
            if i not in st:
                ans.append(i)
        return ans

