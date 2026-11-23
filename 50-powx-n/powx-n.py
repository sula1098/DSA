class Solution:
    def myPow(self, x, n):
        negative = n < 0
        n = abs(n)

        result = 1.0

        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return 1.0 / result if negative else result