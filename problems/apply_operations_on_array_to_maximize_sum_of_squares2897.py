class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        bit_counts = [0] * 30

        for value in nums:
            for bit in range(30):
                bit_counts[bit] += (value >> bit) & 1

        answer = 0
        for _ in range(k):
            value = 0
            for bit in range(30):
                if bit_counts[bit]:
                    value |= 1 << bit
                    bit_counts[bit] -= 1
            answer = (answer + value * value) % mod

        return answer
