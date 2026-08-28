class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        if sum(cnt & 1 for cnt in freq) > 1:
            return ""

        mid = next(
            (i for i, cnt in enumerate(freq) if cnt & 1),
            None
        )


        for i in range(26):
            freq[i] //= 2

        n = len(s)
        half = n // 2

        ans = list(s)

        def make():

            if mid is not None:
                ans[half] = chr(ord('a') + mid)


            for idx in range(half):
                ans[n - 1 - idx] = ans[idx]

        pos = 0


        while pos < half:
            ch = ord(target[pos]) - ord('a')

            if freq[ch] == 0:
                break

            ans[pos] = target[pos]
            freq[ch] -= 1
            pos += 1

        if pos == half:
            make()

            result = ''.join(ans)

            if result > target:
                return result


        while True:
            if pos < half:
                minimum = ord(target[pos]) - ord('a') + 1


                for ch in range(minimum, 26):
                    if freq[ch] != 0:
                        ans[pos] = chr(ord('a') + ch)
                        freq[ch] -= 1


                        dst = pos + 1

                        for c in range(26):
                            cnt = freq[c]

                            for off in range(cnt):
                                ans[dst + off] = chr(ord('a') + c)

                            dst += cnt

                        make()

                        return ''.join(ans)

            if pos == 0:
                return ""

            pos -= 1

            ch = ord(target[pos]) - ord('a')
            freq[ch] += 1