class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time: O(EV) | Space: O(EV)
        adj = [set() for _ in range(numCourses)]  # adjacency list
        for course, prereq in prerequisites:
            adj[prereq].add(course)

        visited = set()
        def dfs(course: int) -> bool:
            if course in visited:
                return False

            visited.add(course)
            for next_course in adj[course]:
                if not dfs(next_course):
                    return False

            visited.remove(course)
            adj[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
