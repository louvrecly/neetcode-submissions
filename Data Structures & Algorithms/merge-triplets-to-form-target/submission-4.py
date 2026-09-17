class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Time: O(n) | Space: O(1)
        conditions = [False] * 3
        for triplet in triplets:
            for i in range(3):
                condition = True
                for j in range(3):
                    condition &= triplet[j] == target[j] if i == j else triplet[j] <= target[j]
                conditions[i] |= condition
        return all(conditions)
