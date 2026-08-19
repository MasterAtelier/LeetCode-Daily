class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:


        n = len(nums)
        dt = {}
        for i in range(n - k + 1):
            for j in range(k):
                if nums[i + j] not in dt:
                    dt[nums[i + j]] = 0
                dt[nums[i + j]] += 1
        max_num = 0
        if k == n:
            return max(nums)
        for key, val in dt.items():
            if val == 1:
                max_num = max(max_num, key)

        return max_num