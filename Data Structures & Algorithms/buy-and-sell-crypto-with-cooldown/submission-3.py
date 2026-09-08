class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        n = len(prices)
        dp = {}  # index -> max profit

        def maxProf(i: int) -> int:
            if i >= n - 1:
                return 0

            if i in dp:
                return dp[i]

            l, r = i, i + 1

            while l < n - 1 and prices[l] >= prices[r]:
                l, r = r, r + 1

            profit = 0
            while r <= n - 1:
                currProfit = prices[r] - prices[l]
                profit = max(profit, currProfit + maxProf(r + 2))
                r += 1

            dp[i] = profit
            return dp[i]

        return maxProf(0)
        # # Time: O(n ** n) | Space: O(n ** n)
        # def maxProf(prices: List[int]) -> int:
        #     n = len(prices)
        #     if n < 2:
        #         return 0

        #     l, r = 0, 1

        #     while l < n - 1 and prices[l] >= prices[r]:
        #         l, r = r, r + 1

        #     profit = 0
        #     while r <= n - 1:
        #         currProf = prices[r] - prices[l]
        #         profit = max(profit, currProf + maxProf(prices[r + 2:]))
        #         r += 1

        #     return profit

        # return maxProf(prices)
