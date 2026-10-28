class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # edges: [[1 2] [1 3] [3 4] [2 4]]
        # 1 - 2
        # |   |
        # 3 - 4
        # -> [2 4]
        # edges: [[1 2] [1 3] [1 4] [3 4] [4 5]]
        # 1 - 2
        # | \
        # 3 - 4 - 5
        # -> [3 4]
        # edges: [[1 2] [1 3] [1 4] [3 4] [4 5]]
        # roots: [1 2 3 4 5] | n: 5
        # [1 2] | r: [1 1 3 4 5]
        # [1 3] | r: [1 1 1 4 5]
        # [1 4] | r: [1 1 1 1 5]
        # [3 4] | r: [1 1 1 1 5] -> [3 4]
        # edges: [[3 4] [1 2] [2 4] [3 5] [2 5]]
        # 5 - 3 - 4
        #   \   /
        # 1 - 2
        # Cycle Detection - Union Find
        # Time: O(E + V) | Space: O(V)
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
                return False

            root = min(root_i, root_j)
            roots[root_i - 1] = root
            roots[root_j - 1] = root
            return True

        for i, j in edges:
            if not union(i, j):
                return [i, j]

        return edges[-1]
