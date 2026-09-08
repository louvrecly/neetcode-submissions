class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # [1 2 3 3]
        #  ^ | 1 { }
        #    ^ | 2 { 1 }
        #      ^ | 3 { 1 2 }
        #        ^ | 3 { 1 2 3 }
        # Time: O(n) | Space: O(1)
        seen = set()  # seen num

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
