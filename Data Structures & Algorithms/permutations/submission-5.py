class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permute([1 2 3])
        # 1 vs permute([2 3])
        #       2 vs permute([3])
        #            3 vs permute([])
        # p([]) -> [[]]
        # p([3]) -> [[ ]] -> [[3]]
        #             ^ 3
        # p([2 3]) -> [[ 3 ]] -> [[2 3] [3 2]]
        #               ^ ^ 2
        # p([1 2 3]) -> [[ 2 3 ] [ 3 2 ]] -> [[1 2 3] [2 1 3] [2 3 1] [1 3 2] [3 1 2] [3 2 1]]
        #                 ^ ^ ^   ^ ^ ^ 1
        # Time: O(n! * n ** 2) | Space: O(n! * n)
        if len(nums) == 0:
            return [[]]

        num = nums[0]
        perms = self.permute(nums[1:])
        results = []

        for perm in perms:
            n = len(perm)
            for i in range(n + 1):
                perm.insert(i, num)
                results.append(perm.copy())
                perm.pop(i)

        return results
