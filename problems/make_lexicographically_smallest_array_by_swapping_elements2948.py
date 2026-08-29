class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        sorted_nums = sorted((value, index) for index, value in enumerate(nums))
        current = [sorted_nums[0]]
        for i in range(1, n):
            if sorted_nums[i][0] - sorted_nums[i - 1][0] <= limit:
                current.append(sorted_nums[i])
            else:
                values = [value for value, _ in current]
                indices = [index for _, index in current]
                indices.sort()
                for j in range(len(indices)):
                    nums[indices[j]] = values[j]
                current = [sorted_nums[i]]
        values = [value for value, _ in current]
        indices = [index for _, index in current]

        indices.sort()

        for j in range(len(indices)):
            nums[indices[j]] = values[j]
        return nums