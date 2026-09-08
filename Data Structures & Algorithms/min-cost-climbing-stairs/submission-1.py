class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1 2 3]
        #  0 1 2 3
        #             Start
        #          1/       \2
        #          0         1
        #       2/   \3   3/   \0
        #       1     2   2     3
        #     3/ \0   |0 0|    [2] <-----
        #     2   3   3   3
        #    0|  [3] [4] [5]
        #     3
        #    [6]
        # [1 2 3]0
        #  0 1 2 3
        #        ^ | 0 | [? ? ? 0]
        #      ^ | 3+0=3 | [? ? 3 0]
        #    ^ | min(2+3,2+0)=2 | [? 2 3 0]
        #  ^ | min(1+2,1+3)=3 | [3 2 3 0]
        #  min(3,2)=2
        # DP
        # Time: O(n) | Space: O(1)
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
