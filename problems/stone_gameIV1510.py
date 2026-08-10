class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for stones in range(1, n + 1):
            k = 1

            while k * k <= stones:
                if not dp[stones - k * k]:
                    dp[stones] = True
                    break

                k += 1

        return dp[n]