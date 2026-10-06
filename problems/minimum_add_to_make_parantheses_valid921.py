class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count_open = 0
        count_close = 0

        for c in s:
            if c == '(':
                count_open += 1
            elif c == ')':
                if count_open > 0:
                    count_open -= 1
                else:
                    count_close += 1

        return count_open + count_close
        