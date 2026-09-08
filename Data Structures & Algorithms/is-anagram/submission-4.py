class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s: jar | t: jam
        #    ^ s{}
        # s: jar | t: jam
        #     ^ s{ j: 1 }
        # s: jar | t: jam
        #      ^ s{ j: 1, a: 1 }
        # s: jar | t: jam
        #       ^ s{ j: 1, a: 1, r: 1 }
        # s: jar | t: jam
        #             ^ t{} | s{ j: 1, a: 1, r: 1 }
        # s: jar | t: jam
        #              ^ t{ j: 1 } | s{ j: 1, a: 1, r: 1 }
        # s: jar | t: jam
        #               ^ t{ j: 1, a: 1 } | s{ j: 1, a: 1, r: 1 }
        # s: jar | t: jam
        #                ^ t{ j: 1, a: 1, m: 1 } | s{ j: 1, a: 1, r: 1 }
        # Time: O(m + n) | Space: O(1)
        return Counter(s) == Counter(t)