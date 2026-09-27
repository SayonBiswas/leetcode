class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        else:
            return x**n