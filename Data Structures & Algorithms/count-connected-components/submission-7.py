class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time: O(E + V) | Space: O(V)
        leaders = list(range(n))

        def findLeader(i: int) -> int:
            while leaders[i] != i:
                i = leaders[i]
            return i

        count = n

        for i, j in edges:
            leader_i = findLeader(i)
            leader_j = findLeader(j)

            if leader_i != leader_j:
                leader = min(leader_i, leader_j)
                leaders[leader_i] = leaders[leader_j] = leader
                count -= 1

        return count
