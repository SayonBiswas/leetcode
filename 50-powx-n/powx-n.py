class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0:
            x, n = (1/x), -n
        while n > 0:
            if n % 2 == 0:
                x *= x
                n //= 2
            elif n % 2 != 0:
                result *= x
                n = n - 1
        return result