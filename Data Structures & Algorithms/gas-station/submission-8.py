class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # g: [1 2 3 4]
        # c: [2 2 4 1]
        #     ^ | 0 +1 -2 = -1 | [0]
        #       ^ | 0 +2 -2 = 0 +3 -4 = -1 | [1 2]
        #         ^ | 0 +3 -4 = -1 | [2]
        #           ^ | 0 +4 -1 = 3 +1 -2 = 2 +2 -2 = 2 +3 -4 = 1 | [3 0 1 2] | r: 3
        # g: [1 2 3]
        # c: [2 3 2]
        #     ^ | 0 +1 -2 = -1 | [0]
        #       ^ | 0 +2 -3 = -1 | [1]
        #         ^ | 0 +3 -2 = 1 +1 -2 = 0 +2 -3 = -1 | [2 0 1]
        # g: [1 2 3 4]
        # c: [2 2 4 1]
        # n: [-1 0 -1 3] | sum: 1 -> has solution!
        #      ^ | t: -1 < 0 | i: 1
        #        ^ | t: 0 = 0 | i: 1
        #           ^ | t: -1 < 0 | i: 2
        #             ^ | t: 3 > 0 | i: 2
        # Time: O(n) | Space: O(1)
        # Init net array (gas[i] - cost[i])
        n = len(gas)

        # Return -1 if sum of net below zero
        if sum(gas) < sum(cost):
            return -1

        # Init tank gas and starting index
        tank = 0
        start = 0

        # Iterate through net array
        for i in range(n):
            # Add net gas to tank
            tank += gas[i] - cost[i]
            # When tank below zero -> reset tank and move starting index to next i
            if tank < 0:
                tank = 0
                start = i + 1

        # Return starting index
        return start
