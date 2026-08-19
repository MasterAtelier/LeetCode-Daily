class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        if n == 1:
            return 0

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for i in range(n - 1, -1, -1):
            p = i - 1

            for j in range(i + 1, n):
                total = prefix[j + 1] - prefix[i]

                while p + 1 < j:
                    next_p = p + 1
                    left_sum = prefix[next_p + 1] - prefix[i]

                    if 2 * left_sum <= total:
                        p = next_p
                    else:
                        break

                best = 0

                if p >= i:
                    best = left_best[i][p]

                    left_sum = prefix[p + 1] - prefix[i]

                    if 2 * left_sum == total:
                        best = max(
                            best,
                            right_best[p + 1][j]
                        )

                if p + 2 <= j:
                    best = max(
                        best,
                        right_best[p + 2][j]
                    )

                dp[i][j] = best

                total_score = best + total

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    total_score
                )

                right_best[i][j] = max(
                    right_best[i + 1][j],
                    total_score
                )

        return dp[0][n - 1]