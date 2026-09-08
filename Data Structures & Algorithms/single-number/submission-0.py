class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # [3 2 3]
        #  ^     | { 3 }
        #    ^   | { 3 2 }
        #      ^ | { 2 }
        # Time: O(n) | Space: O(n)
        found = set()

        for num in nums:
            if num in found:
                found.remove(num)
            else:
                found.add(num)

        return list(found)[0]