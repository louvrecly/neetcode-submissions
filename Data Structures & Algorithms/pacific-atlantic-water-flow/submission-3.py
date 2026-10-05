class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS from edges
        # Time: O(mn) | Space: O(mn)
        m, n = len(heights), len(heights[0])

        def dfs(r: int, c: int, visited: Set[Tuple[int, int]], prev_height=0) -> None:
            if (
                r < 0 or r >= m or
                c < 0 or c >= n or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        pac_set = set()
        atl_set = set()

        for c in range(n):
            dfs(0, c, pac_set)
            dfs(m - 1, c, atl_set)

        for r in range(m):
            dfs(r, 0, pac_set)
            dfs(r, n - 1, atl_set)

        return [[r, c] for r, c in pac_set & atl_set]
