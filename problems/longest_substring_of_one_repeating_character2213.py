from typing import TypeAlias

Node: TypeAlias = list[int | str]


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: list[int]
    ) -> list[int]:

        n = len(s)
        if n == 0:
            return []

        tree: list[Node | None] = [None] * (4 * n)

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = [1, 1, 1, 1, c, c]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            length1, prefix1, suffix1, best1, first1, last1 = left
            length2, prefix2, suffix2, best2, first2, last2 = right

            length = length1 + length2

            best = max(best1, best2)

            prefix = prefix1

            if prefix1 == length1 and last1 == first2:
                prefix = length1 + prefix2

            suffix = suffix2

            if suffix2 == length2 and last1 == first2:
                suffix = length2 + suffix1

            if last1 == first2:
                best = max(best, suffix1 + prefix2)

            return [
                length,
                prefix,
                suffix,
                best,
                first1,
                last2
            ]

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [1, 1, 1, 1, char, char]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)

            assert tree[1] is not None
            answer.append(tree[1][3])

        return answer