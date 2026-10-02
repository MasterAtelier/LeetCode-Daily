class Solution:
    def generate(self, ans: list[str], cur: str, open: int, close: int, max_pairs: int) -> None:
        if len(cur) == max_pairs * 2:
            ans.append(cur)
            return
        if open < max_pairs:
            self.generate(ans, cur + '(', open + 1, close, max_pairs)
        if close < open:
            self.generate(ans, cur + ')', open, close + 1, max_pairs)
    
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        self.generate(ans, "", 0, 0, n)
        return ans