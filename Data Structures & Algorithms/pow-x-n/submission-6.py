class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time: O(log n) | Space: O(log n)
        if x == 1:
            return x

        cache = {}

        def power(num: float, p: int) -> float:
            if p in cache:
                return cache[p]

            if p % 2 == 0:
                cache[p] = 1
            elif p > 0:
                cache[p] = num
            else:
                cache[p] = 1 / num

            q = int(p / 2)
            cache[p] *= power(num, q) * power(num, q)
            return cache[p]

        return power(x, n)
