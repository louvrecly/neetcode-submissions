class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time: O(E + V) | Space: O(V)
        group_ids = [i for i in range(n)]

        for _ in range(n):
            for i, j in edges:
                group_id = min(group_ids[i], group_ids[j])
                group_ids[i] = group_ids[j] = group_id

        ids_set = set(group_ids)
        return len(ids_set)
