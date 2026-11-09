class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(n) | Space: O(n)
        index_map = defaultdict(list)  # mapping num -> (index, gap)[]

        for i, num in enumerate(nums):
            if index_map[num] and i - index_map[num][-1] <= k:
                return True
            index_map[num].append(i)

        return False
