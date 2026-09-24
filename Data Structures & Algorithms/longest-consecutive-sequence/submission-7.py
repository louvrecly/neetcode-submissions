class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        roots = {num: num for num in nums}
        maxLength = 0

        for num, root in roots.items():
            while root - 1 in roots:
                root = roots[root - 1]
            roots[num] = root
            maxLength = max(maxLength, num - root + 1)

        return maxLength
