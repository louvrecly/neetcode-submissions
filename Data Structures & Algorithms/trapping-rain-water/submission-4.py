class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        stack = []  # Monotonic Decreasing Stack (h, i)
        water = 0

        for right, hr in enumerate(height):
            start = right
            while stack and hr > stack[-1][0]:
                floor, left = stack.pop()
                if stack:
                    hl = stack[-1][0]
                    water += (right - left) * (min(hr, hl) - floor)
                    start = left
            stack.append((hr, start))

        return water
