class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # [
        #     [4 2 7 3 4]
        #     [7 4 6 4 7]
        #     [6 3 5 3 6]
        # ]
        # pf: [(0 0) (0 1) (0 2) (0 3) (0 4) (1 0) (2 0)]
        # af: [(0 4) (1 4) (2 0) (2 1) (2 2) (2 3) (2 4)]
        # BFS
        # Time: O(mn) | Space: O(mn)
        m, n = len(heights), len(heights[0])
        pac_frontier = deque([])
        atl_frontier = deque([])

        for c in range(n):
            pac_frontier.append((0, c))
            atl_frontier.append((m - 1, c))

        for r in range(m):
            pac_frontier.append((r, 0))
            atl_frontier.append((r, n - 1))

        steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def bfs(frontier: Deque[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()
            while frontier:
                r, c = frontier.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for step_r, step_c in steps:
                    next_r, next_c = r + step_r, c + step_c
                    if (
                        0 <= next_r < m and
                        0 <= next_c < n and
                        (next_r, next_c) not in visited and
                        heights[next_r][next_c] >= heights[r][c]
                    ):
                        frontier.append((next_r, next_c))
            return visited

        pac_set = bfs(pac_frontier)
        atl_set = bfs(atl_frontier)
        intersection = pac_set & atl_set
        return [[r, c] for r, c in intersection]
