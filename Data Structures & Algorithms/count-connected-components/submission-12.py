class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        # Time: O(E + V) | Space: O(V)
        roots = list(range(n))
        ranks = [1] * n

        def find(i: int) -> int:
            root = i
            while roots[root] != root:
                roots[root] = roots[roots[root]]
                root = roots[root]
            return root

        def union(i: int, j: int) -> int:
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return 0

            if ranks[root_i] > ranks[root_j]:
                roots[root_j] = root_i
                ranks[root_i] += ranks[root_j]
            else:
                roots[root_i] = root_j
                ranks[root_j] += ranks[root_i]

            return 1

        count = n

        for i, j in edges:
            count -= union(i, j)

        return count
