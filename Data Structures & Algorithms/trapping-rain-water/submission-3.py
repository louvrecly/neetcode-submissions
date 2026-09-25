class Solution:
    def trap(self, height: List[int]) -> int:
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
            