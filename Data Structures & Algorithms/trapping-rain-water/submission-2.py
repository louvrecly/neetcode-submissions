class Solution:
    def trap(self, height: List[int]) -> int:
        # [4 2 0 3 2 5]
        #  l         r | 4 < 5 | L: 4 R: 5 | w: 4-2=2 | t: 2
        #    l       r | 2 < 5 | L: 4 R: 5 | w: 4-0=4 | t: 6
        #      l     r | 0 < 5 | L: 4 R: 5 | w: 4-3=1 | t: 7
        #        l   r | 3 < 5 | L: 4 R: 5 | w: 4-2=2 | t: 9
        #          l r | 3 < 5 | L: 4 R: 5 | w: - | t: 9
        # Two Pointers - Opposite Directions (Shrinking Window)
        # Time: O(n) | Space: O(1)
        n = len(height)
        left, right = 0, n - 1
        maxLeft, maxRight = height[left], height[right]
        water = 0

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]

        return water
