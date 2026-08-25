from math import gcd

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        subsets = []
        n = len(coins)

        for i in range(1, 1 << n):
            current_lcm = 1
            count = 0
            for j in range(n):
                if (i >> j) & 1:
                    count += 1
                    current_lcm = (current_lcm * coins[j]) // gcd(current_lcm, coins[j])

            sign = 1 if count % 2 == 1 else -1
            subsets.append((current_lcm, sign))

        def count_amounts_le(target: int) -> int:
            total = 0
            for lcm, sign in subsets:
                total += sign * (target // lcm)
            return total

        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_amounts_le(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans