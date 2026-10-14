class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # n: 2 | p: [[0 1]]
        # 1 -> 0 | True
        # n: 2 | p: [[0 1] [1 0]]
        # 0 -> 1 -> 0 -> 1 -> ... | False
        # Cycle Detection
        # Fast and Slow Pointers vs Post-Order DFS
        # n: 5 | p: [[2 0] [2 1] [3 2] [2 3]]
        # 0   1 4
        #  \ /
        #   2
        #  ( )
        #   3
        # Time: O(EV) | Space: O(EV)
        if not prerequisites:
            return True

        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        def dfs(i: int, visited: Set[int]) -> bool:
            if i in visited:
                return False

            visited.add(i)
            while adj[i]:
                j = adj[i].pop()
                if not dfs(j, visited.copy()):
                    return False

            return True

        for course in adj.copy():
            if not dfs(course, set()):
                return False

        return True
