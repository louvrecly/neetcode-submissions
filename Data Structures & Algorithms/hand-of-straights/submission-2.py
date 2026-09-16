class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1 2 4 2 3 5 3 4] | s: 4
        # [1 2 3 4] [2 3 4 5]
        # [1 2 3 3 4 5 6 7] | s: 4
        # [1 2 3 4] [3 5 6 7]
        # [1 2 4 2 3 5 3 4] | s: 4
        # c: { 1: 1, 2: 2, 3: 2, 4: 2, 5: 1 }
        # [2 4 1 2 3 5 3 4] | s: 4
        #  ^ | 2 | 2-1=1 | [] | c: { 1: 1, 2: 2, 3: 2, 4: 2, 5: 1 }
        #    ^ | 4 | 4-1=3 | [] | c: { 1: 1, 2: 2, 3: 2, 4: 2, 5: 1 }
        #      ^ | 1 | 1-1=0 | [1] | c: { 1: 0, 2: 2, 3: 2, 4: 2, 5: 1 }
        #      ^ | 1 | 1+1=2 | [1 2] | c: { 1: 0, 2: 1, 3: 2, 4: 2, 5: 1 }
        #      ^ | 1 | 2+1=3 | [1 2 3] | c: { 1: 0, 2: 1, 3: 1, 4: 2, 5: 1 }
        #      ^ | 1 | 3+1=4 | [1 2 3 4] | c: { 1: 0, 2: 1, 3: 1, 4: 1, 5: 1 }
        #        ^ | 2 | 2-1=1 | [2] | c: { 1: 0, 2: 0, 3: 1, 4: 1, 5: 1 }
        #        ^ | 2 | 2+1=3 | [2 3] | c: { 1: 0, 2: 0, 3: 0, 4: 1, 5: 1 }
        #        ^ | 2 | 3+1=4 | [2 3 4] | c: { 1: 0, 2: 0, 3: 0, 4: 0, 5: 1 }
        #        ^ | 2 | 4+1=5 | [2 3 4 5] | c: { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }
        # Time: O(n log n) | Space: O(n)
        counter = {}
        for num in hand:
            counter[num] = counter.get(num, 0) + 1

        hand.sort()
        for num in hand:
            if not counter[num]:
                continue
            for i in range(groupSize):
                if not counter.get(num + i, 0):
                    return False
                counter[num + i] -= 1
        return True
