class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        sum = 0
        product = 1
        while n:
            digit = n %10
            sum += digit
            product *= digit
            n //= 10

        return True if num % (sum + product) == 0 else False
        