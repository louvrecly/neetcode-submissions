class Solution:
    def countBits(self, n: int) -> List[int]:
        # n: 4
        # 0: 0 0 0 0 | 0
        # 1: 0 0 0 1 | 1
        # 2: 0 0 1 0 | 1
        # 3: 0 0 1 1 | 2
        # 4: 0 1 0 0 | 1
        # [0 1 1 2 1]
        # 0 1 0 1
        # 0 0 0 1
        # --------&
        # 0 0 0 1
        # # Time: O(n) | Space: O(1)
        counts = []
        for i in range(n + 1):
            count = 0
            while i:
                count += i % 2
                i //= 2
            counts.append(count)
        return counts
        # # Time: O(n) | Space: O(1)
        # counts = []
        # for i in range(n + 1):
        #     count = 0
        #     while i:
        #         count += i & 1
        #         i >>= 1
        #     counts.append(count)
        # return counts
        # # Time: O(n ** 2) | Space: O(n)
        # counts = []
        # for i in range(n + 1):
        #     counts.append(f"{i:b}".count('1'))
        # return counts