class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [2 3 1 1 5 5 4] | k: 3
        # sorted: [1 1 2 3 4 5 5]
        #                  ^ | 4
        # Time: O(n * log n) | Space: O(1)
        nums.sort()
        return nums[-k]
