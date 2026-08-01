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
        

        
    def predictTheWinner(self, nums: list[int]) -> bool:
        dp = {}
        A_Wins = self.predict(0, len(nums) - 1, nums,dp) >= 0
        return True if A_Wins else False

