class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0 3 2 5 4 6 1 1]
        #  ^ | {0:0, 3:3, 2:2, 5:5, 4:4, 6:6, 1:1, 1:1}
        #    ^ | {0:0, 3:0, 2:0, 5:5, 4:4, 6:6, 1:0}
        #      ^ | {0:0, 3:0, 2:0, 5:5, 4:4, 6:6, 1:0}
        #        ^ | {0:0, 3:0, 2:0, 5:0, 4:0, 6:6, 1:0}
        #          ^ | {0:0, 3:0, 2:0, 5:0, 4:0, 6:6, 1:0}
        #            ^ | {0:0, 3:0, 2:0, 5:0, 4:0, 6:0, 1:0}
        #              ^ | {0:0, 3:0, 2:0, 5:0, 4:0, 6:0, 1:0}
        #                ^ | {0:0, 3:0, 2:0, 5:0, 4:0, 6:0, 1:0}
        #                      ^ | 0-0+1=1 | m: 1
        #                           ^ | 3-0+1=4 | m: 4
        #                                ^ | 2-0+1=3 | m: 4
        #                                     ^ | 5-0+1=6 | m: 6
        #                                          ^ | 4-0+1=5 | m: 6
        #                                               ^ | 6-0+1=7 | m: 7
        #                                                    ^ | 1-0+1=2 | m: 7
        # Time: O(n) | Space: O(n)
        roots = {num: num for num in nums}  # Mapping num -> root num
        for num, root in roots.items():
            path = [num]
            while root - 1 in roots:
                root -= 1
                path.append(root)
            for n in path:
                roots[n] = root
        maxLength = 0
        for num, root in roots.items():
            maxLength = max(maxLength, num - root + 1)
        return maxLength
       