class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find
        # Time: O(E + V) | Space: O(E + V)
        n = len(edges)
        roots = [i + 1 for i in range(n)]
        ranks = [1] * n

        def find(i: int) -> int:
            while roots[i - 1] != i:
                roots[i - 1] = roots[roots[i - 1] - 1]
                i = roots[i - 1]
            return i

        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return True

            if ranks[root_i - 1] >= ranks[root_j - 1]:
                roots[root_j - 1] = root_i
                ranks[root_i - 1] += ranks[root_j - 1]
            else:
                roots[root_i - 1] = root_j
                ranks[root_j - 1] = ranks[root_i - 1]

            return False

        for edge in edges:
            if union(*edge):
                return edge