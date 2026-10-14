class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time: O(EV) | Space: O(EV)
        adj = [set() for _ in range(numCourses)]  # adjacency list
        indegrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            adj[prerequisite].add(course)
            indegrees[course] += 1

        frontier = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                frontier.append(course)

        taken = 0
        while frontier:
            course = frontier.popleft()
            taken += 1
            for next_course in adj[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    frontier.append(next_course)

        return taken == numCourses
