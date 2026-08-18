class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = 1
        exponent = abs(n)

        while exponent:
            if exponent & 1:
                result *= x
            x *= x
            exponent >>= 1

        return result if n >= 0 else 1 / result