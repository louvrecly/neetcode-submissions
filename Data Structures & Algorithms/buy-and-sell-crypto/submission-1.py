class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10 1 5 6 7 1]
        #   L R           | 10 < 1 | p: - | maxP: 0
        #     L R         | 1 < 5 | p: 4 | maxP: 4
        #     L   R       | 1 < 6 | p: 5 | maxP: 5
        #     L     R     | 1 < 7 | p: 6 | maxP: 6
        #     L       R   | 1 = 1 | p: - | maxP: 6
        #             L R | 1 = 1 | p: - | maxP: 6
        # Time: O(n) | Space: O(1)
        n = len(prices)
        left, right = 0, 1
        maxProfit = 0

        while left < right < n:
            if prices[left] >= prices[right]:
                left, right = right, right + 1
                continue

            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
            right += 1

        return maxProfit
