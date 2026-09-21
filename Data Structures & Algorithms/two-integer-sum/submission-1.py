class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n: [4 5 6] | t: 10
        #     ^ | 4 | 10-4=6 | { 6: 0 }
        #       ^ | 5 | 10-5=5 | { 6: 0, 5: 1 }
        #         ^ | 6 | T
        # Hash Map
        # Time: O(n) | Space: O(n)
        wanted = {}  # Mapping wanted num -> index

        for i, num in enumerate(nums):
            if num in wanted:
                return [wanted[num], i]
            diff = target - num
            wanted[diff] = i
