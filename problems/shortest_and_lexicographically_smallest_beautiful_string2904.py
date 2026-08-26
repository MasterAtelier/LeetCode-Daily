class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        j = 0
        count_1s = 0
        start = 0
        end = - 1
        for j in range(n):
            if s[j] == '1':
                count_1s += 1
            while count_1s > k:
                if s[i] =='1':
                    count_1s -= 1
                i += 1
            while count_1s == k and s[i] == '0':
                i += 1
            if count_1s == k:
                curr_len = j - i + 1
                if end == -1 or curr_len < end - start + 1:
                    start = i
                    end = j
                elif curr_len == end - start + 1 and s[i : j + 1] < s[start : end + 1]:
                    start = i
                    end = j
        if end == -1:
            return ""
        return s[start : end + 1]
