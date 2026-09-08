class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # p: [1 4 3 2] | h: 9
        #     1 4 3 2 | k: 1 | h: 10 > 9
        #     1 2 2 1 | k: 2 | h: 6 < 9
        #     1 2 1 1 | k: 3 | h: 5 < 9
        # [25 10 23 4] | 4
        #   1  1  1 1  | k: 25 | h: 4 = 4
        # Time: O(n * log n) | Space: O(1)
        n = len(piles)

        left = 1
        right = max(piles)
        minRate = right

        if h == n:
            return minRate

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h:
                left = mid + 1
            else:
                minRate = min(minRate, mid)
                right = mid
        
        return minRate
