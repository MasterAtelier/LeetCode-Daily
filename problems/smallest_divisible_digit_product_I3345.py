class Solution:
    def digit_product(self, n):
        if n < 10:
            return n
        prod = 1
        while n:
            prod *= n % 10
            n = n // 10
        return prod
        
    def smallestNumber(self, n: int, t: int) -> int:

        while self.digit_product(n)% t != 0:
            n += 1
            
        return n
            

