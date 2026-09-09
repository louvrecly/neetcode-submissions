class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n! * n) | Space: O(n! * n)
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        num = nums[0]
        results = []

        for perm in perms:
            n = len(perm)

            for i in range(n + 1):
                perm.insert(i, num)
                results.append(perm.copy())
                perm.pop(i)
        
        return results
        