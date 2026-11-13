class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Linked List Cycle Detection | Fast and Slow Pointers
        # [1 2 3 2 2]
        #  S F
        #    S   F
        #      S F
        #       SF   | 2
        # [1 2 3 4 4]
        #  S F
        #    S   F
        #      S   F
        #        S F
        #         SF | 4
        # [1 3 4 2 2]
        #  S F
        #    S F
        #      F S
        #     SF
        # Time: O(n) | Space: O(1)
        slow = nums[nums[0]]
        fast = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        pointer = nums[0]
        while pointer != slow:
            pointer = nums[pointer]
            slow = nums[slow]

        return pointer
