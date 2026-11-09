class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(n) | Space: O(n)
        index_map = defaultdict(list)  # mapping num -> index[]

        for i, num in enumerate(nums):
            index_map[num].append(i)

        keys = list(index_map.keys())
        for num in keys:
            indexes = index_map[num]
            if len(indexes) < 2:
                continue
            
            prev = indexes[0]
            for i in range(1, len(indexes)):
                if indexes[i] - prev <= k:
                    return True
                prev = indexes[i]

        return False