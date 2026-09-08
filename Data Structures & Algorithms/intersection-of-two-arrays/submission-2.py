class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(m + n) | Space: O(m + n)
        set1, set2 = set(nums1), set(nums2)
        return list(set1.intersection(set2))
        # # Time: O(m + n) | Space: O(m + n)
        # set1, set2 = set(nums1), set(nums2)
        # result = []
        # for num in set1:
        #     if num in set2:
        #         result.append(num)
        # return result