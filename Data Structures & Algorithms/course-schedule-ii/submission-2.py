class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sort - Post-Order DFS
        # Time: O(E + V) | Space: O(E + V)
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        topology = []
        visiting = {}  # Mapping course -> True=visiting | False=visited

        def dfs(course: int) -> bool:
            if course in visiting:
                return visiting[course]

            visiting[course] = True
            for next_course in adj[course]:
                if dfs(next_course):
                    return True

            topology.append(course)
            visiting[course] = False

        for course in range(numCourses):
            if dfs(course):
                return []

        topology.reverse()
        return topology
