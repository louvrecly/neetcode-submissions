class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # nums: [2 4]
        # 2: 0010
        # 4: 0100
        # --------XOR
        # 6: 0110
        # 2: 0010
        # 4: 0100
        # --------SUM
        # 12:1100
        # nums: [3 1 1]
        # 3: 0011
        # 1: 0001
        # [3]:3 [1]:1 [1]:1
        # [3 1]:3^1=2 [3 1]:3^1=2 [1 1]:1^1=0
        # [3 1 1]:3^1^1=3
        # sum: 3+1+1+2+2+0+3=12
        # nums: [3 1 1]
        #        ^ | [3] []
        #          ^ | [3 1] [3]
        #            ^ | [3 1 1] [3 1]
        #            ^ | [3 1] [3]
        #          ^ | [1] []
        #            ^ | [1 1] [1]
        #             ^ | [1] []
        # dp(i, prev) = dp(i + 1, prev + [nums[i]]) + dp(i + 1, prev)
        # Time: O(n^2) | Space: O(n^2)
        n = len(nums)

        def dp(i: int, prev: List[int]) -> int:
            if i >= n:
                result = 0
                for num in prev:
                    result ^= num
                return result

            return dp(i + 1, prev + [nums[i]]) + dp(i + 1, prev)

        return dp(0, [])
