class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS with frontier queue, adjacency list, and indegrees
        # Time: O(E + V^2) | Space: O(E + V)
        adj = {course: [] for course in range(numCourses)}
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1

        frontier = deque()

        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                frontier.append(course)

        taken = 0
        topo = []

        while frontier:
            course = frontier.popleft()
            taken += 1
            topo.append(course)

            for next_course in adj[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    frontier.append(next_course)

        return topo if taken == numCourses else []
