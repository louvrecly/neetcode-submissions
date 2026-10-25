class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find
        # Time: O(E + V) | Space: O(V)
        roots = list(range(n))
        ranks = [1] * n

        def find(i: int) -> int:
            breadcrumb = []
            while roots[i] != i:
                breadcrumb.append(i)
                i = roots[i]

            for j in breadcrumb:
                if roots[j] != i:
                    roots[j] = i
            return i

        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return False

            if ranks[root_i] > ranks[root_j]:
                roots[root_j] = root_i
                ranks[root_i] += 1
            else:
                roots[root_i] = root_j
                ranks[root_j] += 1

            return True

        count = n

        for i, j in edges:
            if union(i, j):
                count -= 1

        return count
