class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        # Time: O(E + V) | Space: O(V)
        roots = list(range(n))
        ranks = [1] * n

        def find(i: int) -> int:
            while roots[i] != i:
                i = roots[i]
            return i

        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return False

            if ranks[root_i] > ranks[root_j]:
                roots[root_j] = root_i
            else:
                roots[root_i] = root_j

            return True

        count = n

        for i, j in edges:
            if union(i, j):
                count -= 1

        return count
