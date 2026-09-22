class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #    [1 7 2 5 4 7 3 6]
        # 7 |   X       X
        # 6 |   X       X   X
        # 5 |   X   X   X   X
        # 4 |   X   X X X   X
        # 3 |   X   X X X X X
        # 2 |   X X X X X X X
        # 1 | X X X X X X X X
        # 0 | 0 1 2 3 7 5 6 7
        # #  L R | w: 1-0=1 
        # [1 7 2 5 4 7 3 6]
        #  L             R | w: 7-0=7 h: min(1,6)=1 | a: 7*1=7 | m: 7
        #    L           R | w: 7-1=6 h: min(7,6)=6 | a: 6*6=36 | m: 36
        #    L         R | w: 6-1=5 h: min(7,3)=3 | a: 5*3=15 | m: 36
        #    L       R | w: 5-1=4 h: min(7,7)=7 | a: 4*7=28 | m: 36
        #    L       R | w: 5-1=4 h: min(7,7)=7 | a: 4*7=28 | m: 36
        # Time: O(n) | Space: O(1)
        n = len(heights)
        left, right = 0, n - 1
        area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = max(area, width * height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area
