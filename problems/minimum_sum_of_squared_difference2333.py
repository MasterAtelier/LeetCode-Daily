class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        differences = [abs(a - b) for a, b in zip(nums1, nums2)]
        operations = k1 + k2

        if sum(differences) <= operations:
            return 0

        low, high = 0, max(differences)
        while low < high:
            middle = (low + high) // 2
            required = sum(max(diff - middle, 0) for diff in differences)
            if required <= operations:
                high = middle
            else:
                low = middle + 1

        cap = low
        used = sum(max(diff - cap, 0) for diff in differences)
        remaining = operations - used
        result = sum(min(diff, cap) ** 2 for diff in differences)

        # The remaining operations lower distinct values from cap to cap - 1.
        return result - remaining * (2 * cap - 1)
