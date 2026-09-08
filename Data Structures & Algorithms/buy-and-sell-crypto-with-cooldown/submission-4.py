class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # not holding -> (buy vs wait)
        # holding -> (sell vs wait)
        # DP: memo { (index, holding) -> max profit }
        n = len(prices)
        dp = {}

        def maxProfitAt(i: int, holding: bool) -> int:
            if i > n - 1:
                return 0

            if (i, holding) in dp:
                return dp[(i, holding)]

            waitProfit = maxProfitAt(i + 1, holding)
            if holding:
                sellProfit = maxProfitAt(i + 2, False) + prices[i]
                dp[(i, holding)] = max(waitProfit, sellProfit)
            else:
                buyProfit = maxProfitAt(i + 1, True) - prices[i]
                dp[(i, holding)] = max(waitProfit, buyProfit)

            return dp[(i, holding)]

        return maxProfitAt(0, False)
