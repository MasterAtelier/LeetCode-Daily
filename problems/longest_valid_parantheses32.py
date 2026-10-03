class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        last_invalid_index = -1

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if not stack:
                    last_invalid_index = i
                else:
                    stack.pop()
                    if not stack:
                        max_length = max(max_length, i - last_invalid_index)
                    else:
                        max_length = max(max_length, i - stack[-1])

        return max_length

        