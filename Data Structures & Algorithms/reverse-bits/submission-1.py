class Solution:
    def reverseBits(self, n: int) -> int:
        # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 0
        # 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        # n -> b: string -> reverse -> parse as integer
        # Time: O(1) | Space: O(1)
        binString = f"{n:b}"
        leadingZeroCount = 32 - len(binString)
        return int(binString[::-1] + '0' * leadingZeroCount, 2)
