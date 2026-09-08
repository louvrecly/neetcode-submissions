class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time: O(1) | Space: O(1)
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count
        # # # Time: O(1) | Space: O(1)
        # count = 0
        # while n > 0:
        #     count += n % 2
        #     n //= 2
        # return count
        # # Time: O(1) | Space: O(1)
        # count = 0
        # while n > 0:
        #     count += n & 1
        #     n >>= 1
        # return count
        # # Time: O(n) | Space: O(n)
        # return f"{n:b}".count('1')
