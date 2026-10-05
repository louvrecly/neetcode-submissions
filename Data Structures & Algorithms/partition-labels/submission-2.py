class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # s: xyxxyzbzbbisl
        # x y x x y z b z b b i s l
        # r: {x:3 y:2 z: 2 b: 3 i:1 s:1 l:1}
        # x y x x y z b z b b i s l
        # LR | x | c: {x:1} | r: {x:3 y:2 z:2 b:3 i:1 s:1 l:1} | m: 0 < l: 1 | []
        # L R | xy | c: {x:1 y:1} | r: {x:2 y:2 z:2 b:3 i:1 s:1 l:1} | m: 0 < l: 2 | []
        # L R | xy | c: {x:1 y:1} | r: {x:2 y:1 z:2 b:3 i:1 s:1 l:1} | m: 0 < l: 2 | []
        # L   R | xyx | c: {x:2 y:1} | r: {x:1 y:1 z:2 b:3 i:1 s:1 l:1} | m: 0 < l: 2 | []
        # L     R | xyxx | c: {x:3 y:1} | r: {x:0 y:1 z:2 b:3 i:1 s:1 l:1} | m: 1 < l: 2 | []
        # L       R | xyxxy | c: {x:3 y:2} | r: {x:0 y:1 z:2 b:3 i:1 s:1 l:1} | m: 2 = l: 2 | [5]
        #           LR | z | c: {z:1} | r: {x:0 y:1 z:1 b:3 i:1 s:1 l:1} | m: 0 < l: 1 | [5]
        #           L R | zb | c: {z:1 b:1} | r: {x:0 y:1 z:1 b:2 i:1 s:1 l:1} | m: 0 < l: 2 | [5]
        #           L   R | zbz | c: {z:2 b:1} | r: {x:0 y:1 z:0 b:2 i:1 s:1 l:1} | m: 1 < l: 2 | [5]
        #           L     R | zbzb | c: {z:2 b:2} | r: {x:0 y:1 z:0 b:1 i:1 s:1 l:1} | m: 1 < l: 2 | [5]
        #           L       R | zbzbb | c: {z:2 b:3} | r: {x:0 y:1 z:0 b:0 i:1 s:1 l:1} | m: 2 = l: 2 | [5 5]
        #                     LR | i | c: {i:1} | r: {x:0 y:1 z:0 b:0 i:0 s:1 l:1} | m: 1 = l: 1 | [5 5 1]
        #                       LR | s | c: {s:1} | r: {x:0 y:1 z:0 b:0 i:0 s:0 l:1} | m: 1 = l: 1 | [5 5 1 1]
        #                         LR | l | c: {l:1} | r: {x:0 y:1 z:0 b:0 i:0 s:0 l:0} | m: 1 = l: 1 | [5 5 1 1 1]
        # Sliding Window -> Same Direction (Left to Right)
        # Time: O(n) | Space: O(n)
        rest_counts = {}  # Mapping char -> count
        for char in s:
            rest_counts[char] = rest_counts.get(char, 0) + 1

        curr_counts = {}
        matches = 0
        left = 0
        result = []
        for right in range(len(s)):
            char = s[right]
            curr_counts[char] = curr_counts.get(char, 0) + 1
            rest_counts[char] -= 1
            if rest_counts[char] == 0:
                matches += 1
                if matches == len(curr_counts):
                    result.append(right - left + 1)
                    left = right + 1
                    curr_counts = {}
                    matches = 0

        return result
