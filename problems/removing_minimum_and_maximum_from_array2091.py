class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        max_val_idx_pair = (nums[0], 0)
        min_val_idx_pair = (nums[0], 0)
        for i in range(n):
            if nums[i] > max_val_idx_pair[0]:
                max_val_idx_pair = (nums[i], i)
            if nums[i] < min_val_idx_pair[0]:
                min_val_idx_pair = (nums[i], i)

        left = min(max_val_idx_pair[1], min_val_idx_pair[1])
        right = max(max_val_idx_pair[1], min_val_idx_pair[1])
        num_deletions = min(right + 1, n - left, left + 1 + n - right)
        return num_deletions