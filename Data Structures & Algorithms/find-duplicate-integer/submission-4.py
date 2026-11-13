class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Linked List Cycle Detection | Fast and Slow Pointers
        # [1 3 4 2 2]
        #  S F
        #    S F
        #      F S
        #     SF
        #  P   S
        #    P     S
        #      S P
        #      P   S
        #      S   P
        #      P   S
        #      S   P
        # [1 3 4 2 2]
        # SF
        #    S   F   | 3 vs 4
        #        S F | 2 == 2
        #  P     S   | 1 vs 2
        #    P S     | 3 vs 4
        #        P S | 2 == 2
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
