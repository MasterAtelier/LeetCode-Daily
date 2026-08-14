class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        i = 0
        j = 0
        dt = {}
        while j < n:
            if s[j] not in dt:
                dt[s[j]] = 1
            else:
                dt[s[j]]  += 1

            while dt[s[j]] > 2:
                dt[s[i]] -= 1
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len  