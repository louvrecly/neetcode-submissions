class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP
        # Time: O(n) | Space: O(1)
        n = len(cost)
        c1, c2 = cost[n - 1], 0

        for i in range(n - 2, -1, -1):
            c1, c2 = cost[i] + min(c1, c2), c1

        return min(c1, c2)
