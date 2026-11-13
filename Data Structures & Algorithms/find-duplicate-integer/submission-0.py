class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n: [1 2 3 2 2]
        # counter: {1:1, 2:3, 3:1, 4:0} | 2
        # n: [1 2 3 4 4]
        # counter: {1:1, 2:1, 3:1, 4:2} | 4
        # Time: O(n) | Space: O(n)
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return num
            nums_set.add(num)
