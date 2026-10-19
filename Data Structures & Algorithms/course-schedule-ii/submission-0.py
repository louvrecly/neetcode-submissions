class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # n: 3 | p: [[1 0]]
        # 0 -> 1
        # 2
        # n: 3 | p: [[0 1] [1 2] [2 0]]
        # 1 -> 0
        #  ^  v
        #    2
        # Find non-cyclical path
        # adjacency list + indegrees
        # n: 6 | p: [[1 0] [2 1] [3 2] [1 3] [3 4]]
        # 0 -> 1 -> 2  5
        #       ^  v
        #    4 -> 3
        # adj: { 0:[1] 1:[2] 2:[3] 3:[1] 4:[3] 5:[] } | ind: { 0:0 1:1 2:1 3:2 4:0 5:0 }
        # Post-order DFS pruning edges in adj
        # starters: [0 4 5]
        # 0 | adj: { 0:[1] 1:[2] 2:[3] 3:[1] 4:[3] 5:[] } | v: {0} -> []
        # 1 | adj: { 0:[] 1:[2] 2:[3] 3:[1] 4:[3] 5:[] } | v: {0 1} -> []
        # 2 | adj: { 0:[] 1:[] 2:[3] 3:[1] 4:[3] 5:[] } | v: {0 1 2} -> []
        # 3 | adj: { 0:[] 1:[] 2:[] 3:[1] 4:[3] 5:[] } | v: {0 1 2 3} -> []
        # 1 | adj: { 0:[] 1:[] 2:[] 3:[1] 4:[3] 5:[] } | v: {0 1 2 3} -> []
        # ==================================================================
        # n: 6 | p: [[1 0] [2 1] [3 1] [3 2] [4 3]]
        # 0 -> 1 -> 2  5
        #       v  v
        #         3 -> 4
        # adj: { 0:[1] 1:[2 3] 2:[3] 3:[4] 4:[] 5:[] } | ind: { 0:0 1:1 2:1 3:2 4:1 5:0 }
        # Post-order DFS pruning edges in adj
        # starters: [0 5]
        # 0 | adj: { 0:[1] 1:[2 3] 2:[3] 3:[4] 4:[] 5:[] } | v: {0} -> []
        # 1 | adj: { 0:[] 1:[2 3] 2:[3] 3:[4] 4:[] 5:[] } | v: {0 1} -> []
        # 2 | adj: { 0:[] 1:[3] 2:[3] 3:[4] 4:[] 5:[] } | v: {0 1 2} -> []
        # 3 | adj: { 0:[] 1:[3] 2:[] 3:[4] 4:[] 5:[] } | v: {0 1 2 3} -> []
        # 4 | adj: { 0:[] 1:[3] 2:[] 3:[] 4:[] 5:[] } | v: {0 1 2 3 4} -> [4]
        # 3 | adj: { 0:[] 1:[3] 2:[] 3:[] 4:[] 5:[] } | v: {0 1 2 3 4} -> [4 3]
        # 2 | adj: { 0:[] 1:[3] 2:[] 3:[] 4:[] 5:[] } | v: {0 1 2 3 4} -> [4 3 2]
        # 1 | adj: { 0:[] 1:[3] 2:[] 3:[] 4:[] 5:[] } | v: {0 1 2 3 4} -> [4 3 2]
        # 3 | adj: { 0:[] 1:[] 2:[] 3:[] 4:[] 5:[] } | v: {0 1 2 3 4} -> [4 3 2 3]
        # 1 | adj: { 0:[] 1:[] 2:[] 3:[] 4:[] 5:[] } | v: {0 1 2 3 4} -> [4 3 2 3 1]
        # 5 | adj: { 0:[] 1:[] 2:[] 3:[] 4:[] 5:[] } | v: {0 1 2 3 4 5} -> [4 3 2 3 1 5]
        # reversed: [5 1 3 2 3 4]
        # Time: O(E + V^2) | Space: O(E + V^2)
        adj = {course: [] for course in range(numCourses)}
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1

        starters = []
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                starters.append(course)

        visiting = {}  # Mapping course -> True=visiting | False=visited
        sequence = []

        def dfs(course: int) -> bool:
            if course in visiting:
                return visiting[course]

            visiting[course] = True

            while adj[course]:
                neighbor = adj[course].pop()
                if dfs(neighbor):
                    return True

            sequence.append(course)
            visiting[course] = False

        for starter in starters:
            if dfs(starter):
                return []

        sequence.reverse()
        return sequence
