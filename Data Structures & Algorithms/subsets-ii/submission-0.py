class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # [1 2 1]
        # sorted: [1 1 2]
        #                        [ ]
        #                /                \
        #              [1]                [ ]
        #          /        \           /     \
        #      [1 1]        [1]       [1]     [ ]
        #       / \         / \       / \     / \
        # [1 1 2] [1 1] [1 2] [1] [1 2] [1] [2] [ ]
        # Time: O(n * 2 ** n) | Space: O(n * 2 ** n)
        if len(nums) == 0:
            return [[]]

        nums.sort()
        num = nums.pop()
        subsets = self.subsetsWithDup(nums)

        results = subsets.copy()
        for subset in subsets:
            subsetCopy = subset.copy()
            subsetCopy.append(num)
            results.append(subsetCopy)

        tuplesSet = set([tuple(result) for result in results])
        return [list(tupleSet) for tupleSet in tuplesSet]
