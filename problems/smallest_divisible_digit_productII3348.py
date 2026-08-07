from collections import Counter

class Solution:
    FACTOR_COUNTS = {
        0: Counter(),
        1: Counter(),
        2: Counter({2: 1}),
        3: Counter({3: 1}),
        4: Counter({2: 2}),
        5: Counter({5: 1}),
        6: Counter({2: 1, 3: 1}),
        7: Counter({7: 1}),
        8: Counter({2: 3}),
        9: Counter({3: 2}),
    }

    def getPrimeCount(self, t: int):
        count = Counter({2: 0, 3: 0, 5: 0, 7: 0})
        for p in (2, 3, 5, 7):
            while t % p == 0:
                count[p] += 1
                t //= p
        return count, t == 1

    def getPrimeCountFromString(self, num: str):
        count = Counter({2: 0, 3: 0, 5: 0, 7: 0})
        for ch in num:
            count += self.FACTOR_COUNTS[int(ch)]
        return count

    def subtract(self, a: Counter, b: Counter):
        res = Counter(a)
        for k, v in b.items():
            res[k] = max(0, res[k] - v)
        return res

    def isSubset(self, need: Counter, have: Counter):
        for p in (2, 3, 5, 7):
            if have[p] < need[p]:
                return False
        return True

    def sumValues(self, cnt):
        return sum(cnt.values())

    def getFactorCount(self, cnt: Counter):
        res = Counter()

        count8 = cnt[2] // 3
        rem2 = cnt[2] % 3

        count9 = cnt[3] // 2
        rem3 = cnt[3] % 2

        count4 = rem2 // 2
        count2 = rem2 % 2

        count6 = 0

        if count2 == 1 and rem3 == 1:
            count2 = 0
            rem3 = 0
            count6 = 1

        if rem3 == 1 and count4 == 1:
            count2 = 1
            count6 = 1
            rem3 = 0
            count4 = 0

        res[2] = count2
        res[3] = rem3
        res[4] = count4
        res[5] = cnt[5]
        res[6] = count6
        res[7] = cnt[7]
        res[8] = count8
        res[9] = count9

        return res

    def construct(self, factors: Counter):
        ans = []
        for digit in range(2, 10):
            ans.extend(str(digit) for _ in range(factors[digit]))
        return "".join(ans)

    def smallestNumber(self, num: str, t: int) -> str:
        primeCount, ok = self.getPrimeCount(t)
        if not ok:
            return "-1"

        factorCount = self.getFactorCount(primeCount)

        if self.sumValues(factorCount) > len(num):
            return self.construct(factorCount)

        primePrefix = self.getPrimeCountFromString(num)

        firstZero = num.find('0')
        if firstZero == -1:
            firstZero = len(num)
            if self.isSubset(primeCount, primePrefix):
                return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])

            primePrefix = self.subtract(
                primePrefix,
                self.FACTOR_COUNTS[d]
            )

            space = len(num) - 1 - i

            if i > firstZero:
                continue

            for bigger in range(d + 1, 10):

                need = self.subtract(
                    self.subtract(primeCount, primePrefix),
                    self.FACTOR_COUNTS[bigger]
                )

                factors = self.getFactorCount(need)

                if self.sumValues(factors) <= space:
                    fill = space - self.sumValues(factors)

                    return (
                        num[:i]
                        + str(bigger)
                        + "1" * fill
                        + self.construct(factors)
                    )

        factors = self.getFactorCount(primeCount)

        return (
            "1" * (len(num) + 1 - self.sumValues(factors))
            + self.construct(factors)
        )