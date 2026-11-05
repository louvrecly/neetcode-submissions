class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums: [1 4 1 2]
        # [1 4 1 2 1 4 1 2]
        # Time: O(n) | Space: O(1)
        return nums + nums