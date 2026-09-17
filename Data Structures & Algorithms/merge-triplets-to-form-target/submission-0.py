class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # [
        #     [1 2 3]
        #     [7 1 1]
        # ] | t: [7 2 3]
        # 0: [1 2 3] | [1<7 2=2 3=3] | [0] | { 1 2 }
        # 1: [7 1 1] | [7=7 1<2 1<1] | [0 1] | { 0 1 2 } -> T
        # [
        #     [2 5 6]
        #     [1 4 4]
        #     [5 0 5]
        #     [3 4 6]
        # ] | : [5 4 6]
        # 0: [2 5 6] | [2<5 5>4 6=6] | [] | {}
        # 1: [1 4 4] | [1<5 4=4 4<6] | [1] | {1}
        # 2: [5 0 5] | [5=5 0<4 5<6] | [1 2] | {0 1}
        # 3: [3 4 6] | [3<5 4=4 6=6] | [1 2 3] | {0 1 2} -> T
        # Time: O(n) | Space: O(1)
        matches = set()  # matched indexes i
        at, bt, ct = target
        for ai, bi, ci in triplets:
            diffA = at - ai
            diffB = bt - bi
            diffC = ct - ci
            if diffA < 0 or diffB < 0 or diffC < 0:
                continue
            if diffA == 0:
                matches.add(0)
            if diffB == 0:
                matches.add(1)
            if diffC == 0:
                matches.add(2)
            if len(matches) == 3:
                return True
        return False
