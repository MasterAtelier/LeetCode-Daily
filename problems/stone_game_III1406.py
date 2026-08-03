class Solution:
    def predict(self,i, n, nums, dp):
            if i > n:
                return 0
            
            if i in dp:
                return dp[i]

            best = float("-inf")

            curr = 0
            for k in range(3):
                if i + k > n:
                    break
                curr += nums[i + k]
                best = max(best, curr - self.predict(i + k + 1, n, nums, dp))

            
            dp[i] = best
            return dp[i]

      
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        dp = {}
        prediction = self.predict(0, len(stoneValue) -  1,  stoneValue, dp)
        if prediction > 0:
            return "Alice"
        elif prediction < 0:
            return "Bob"
        return "Tie"


         

        