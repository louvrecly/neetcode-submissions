class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n! * n ** 2) | Space: O(n! * n)
        perms = [[]]

        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    p = perm.copy()
                    p.insert(i, num)
                    new_perms.append(p)
            perms = new_perms

        return perms
