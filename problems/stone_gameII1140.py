class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

      
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i: int, M: int) -> int:
    
            if i == n:
                return 0

           
            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

       
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                new_M = max(M, X)

                current = suffix[i] - solve(i + X, new_M)

                best = max(best, current)

            dp[(i, M)] = best
            return best

        return solve(0, 1)