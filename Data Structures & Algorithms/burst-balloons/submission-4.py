class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # n: [4 2 3 7]
        #     ^ | 1*4*2=8 [2 3 7]
        #       ^ | 4*2*3=24 [4 3 7]
        #         ^ | 2*3*7=42 [4 2 7]
        #           ^ | 3*7*1=21 [4 2 3]
        #                           [4 2 3 7]
        #            /              |       |    \
        #      [2 3 7]           [4 3 7] [4 2 7] [4 2 3]
        #     /   |   \         /   |   \    /   |   \    /   |   \
        # [3 7] [2 7] [2 3] [3 7] [4 7] [3 7] 
        # [4 2 3 7]
        # [1 4 2 3 7 1]
        #    L     R
        #    ^ | 
        # dp(L,R) = n[i-1]*n[i]*n[i+1] + dp(1,1) + dp(2,4) for i in range(1, n - 1)
        # Time: O(n^3) | Space: O(n^2)
        vals = [1] + nums + [1]
        memo = {}
        def dp(left: int, right: int) -> int:
            if left > right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            result = 0
            for i in range(left, right + 1):
                result = max(
                    result,
                    vals[left - 1] * vals[i] * vals[right + 1] +
                    dp(left, i - 1) +
                    dp(i + 1, right)
                )

            memo[(left, right)] = result
            return memo[(left, right)]

        return dp(1, len(nums))
