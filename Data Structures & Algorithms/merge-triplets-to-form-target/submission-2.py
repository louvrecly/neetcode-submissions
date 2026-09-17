class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Time: O(n) | Space: O(1)
        matches = set()
        for triplet in triplets:
            currentMatches = []
            skip = False
            for i in range(3):
                if triplet[i] > target[i]:
                    skip = True
                    break
                if triplet[i] == target[i]:
                    currentMatches.append(i)
            if not skip:
                matches.update(currentMatches)
                if len(matches) == 3:
                    return True
        return False
