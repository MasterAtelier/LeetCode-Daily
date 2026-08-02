class Solution:
    def predict(self,i, j, nums, dp ):
            if i > j:
                return 0
            if i == j:
                return nums[i]
            state = (i, j)
            if state not in dp:
                dp[state] = max(
                    nums[i] - self.predict(i + 1, j, nums, dp),
                    nums[j] - self.predict(i, j - 1, nums, dp)
                )
    
            return dp[state]
    def stoneGame(self, piles: list[int]) -> bool:
         dp = {}
         return self.predict(0, len(piles) - 1, piles, dp) > 0

        