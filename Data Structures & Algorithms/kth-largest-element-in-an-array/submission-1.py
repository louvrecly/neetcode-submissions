class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n + k) | Space: O(1)
        heapq.heapify_max(nums)
        for i in range(k - 1):
            num = heapq.heappop_max(nums)
        return nums[0]
