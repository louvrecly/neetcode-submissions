class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Time: O(n) | Space: O(1)
        matches = set()
        for triplet in triplets:
            skip = any([triplet[i] > target[i] for i in range(3)])
            if skip:
                continue
            for i in range(3):
                if triplet[i] == target[i]:
                    matches.add(i)
            if len(matches) == 3:
                return True
        return False
