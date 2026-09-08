class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # z x y z w y y z
        # LR | setL: 1 = l: 1 | maxL: 1
        # z x y z w y y z
        # L R | setL: 2 = l: 2 | maxL: 2
        # z x y z w y y z
        # L   R | setL: 3 = l: 3 | maxL: 3
        # z x y z w y y z
        # L     R | setL: 3 < l: 4 | maxL: 3
        # z x y z w y y z
        #   L   R | setL: 3 = l: 3 | maxL: 3
        # z x y z w y y z
        #   L     R | setL: 4 = l: 4 | maxL: 4
        # z x y z w y y z
        #   L       R | setL: 4 < l: 5 | maxL: 4
        # z x y z w y y z
        #     L     R | setL: 3 < l: 4 | maxL: 4
        # z x y z w y y z
        #       L   R | setL: 3 = l: 3 | maxL: 4
        # z x y z w y y z
        #       L     R | setL: 3 < l: 4 | maxL: 4
        # z x y z w y y z
        #         L   R | setL: 2 < l: 3 | maxL: 4
        # z x y z w y y z
        #           L R | setL: 1 < l: 2 | maxL: 4
        # z x y z w y y z
        #             LR | setL: 1 = l: 1 | maxL: 4
        # z x y z w y y z
        #             L R | setL: 2 = l: 2 | maxL: 4
        # Sliding Window
        # Time: O(n) | Space: O(n)
        n = len(s)
        if n == 0:
            return 0
        
        l, r = 0, 0
        maxLength = 0
        counter = defaultdict(int)  # Mapping char -> count
        charSet = set()  # chars set in window
        
        char = s[r]
        counter[char] += 1
        charSet.add(char)

        while l < n:
            while len(charSet) == r - l + 1:
                r += 1
                if r < n:
                    char = s[r]
                    counter[char] += 1
                    charSet.add(char)

            maxLength = max(maxLength, r - l)
            char = s[l]
            counter[char] -= 1
            if counter[char] == 0:
                charSet.remove(char)
            l += 1

        return maxLength