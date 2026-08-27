from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        n = len(s)
        

        ans = []
        
        def solve(idx: int, is_greater: bool) -> bool:
            if idx == n:
                return is_greater
            
            if is_greater:
                for c in range(26):
                    char = chr(ord('a') + c)
                    if counts[char] > 0:
                        counts[char] -= 1
                        ans.append(char)
                        if solve(idx + 1, True):
                            return True
                        ans.pop()
                        counts[char] += 1
                return False
            

            target_char = target[idx]
            

            if counts[target_char] > 0:
                counts[target_char] -= 1
                ans.append(target_char)
                if solve(idx + 1, False):
                    return True
                ans.pop()
                counts[target_char] += 1
                

            for c in range(ord(target_char) - ord('a') + 1, 26):
                char = chr(ord('a') + c)
                if counts[char] > 0:
                    counts[char] -= 1
                    ans.append(char)
                    if solve(idx + 1, True):
                        return True
                    ans.pop()
                    counts[char] += 1
                    
            return False

        if solve(0, False):
            return "".join(ans)
        return ""

