class Solution:
    def isHappy(self, n: int) -> bool:
        # n: 100
        # 1 0 0 | 1+0+0=1 | True
        # n: 101
        # 1 0 1 | 1+0+1=2
        # 2 | 4=4
        # 4 | 16
        # 1 6 | 1+36=37
        # 3 7 | 9+49=58
        # 5 8 | 25+64=89
        # 8 9 | 64+81=145
        # 1 4 5 | 1+16+25=42
        # 4 2 | 16+4=20
        # 2 0 | 4+0=4
        # 4 | False
        # Time: O(cycle) | Space: O(cycle)
        nums_set = set()

        while n != 1:
            if n in nums_set:
                return False
            nums_set.add(n)
            num = 0
            while n:
                num += (n % 10) ** 2
                n //= 10
            n = num
        return True
