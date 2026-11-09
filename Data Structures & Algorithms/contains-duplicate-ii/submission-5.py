class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(n) | Space: O(n)
        index_map = defaultdict(list)  # mapping num -> (index, gap)[]

        for i, num in enumerate(nums):
            gap = i - index_map[num][-1][0] if index_map[num] else float('inf')
            index_map[num].append((i, gap))

        for indexes in index_map.values():
            for _, gap in indexes:
                if gap <= k:
                    return True

        return False
