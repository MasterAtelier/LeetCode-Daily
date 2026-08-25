class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        num_set = set(nums)
        prod = k
        while prod in num_set:
            prod += k
        return prod
            
        