class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # num1: 23 | num2: 44
        # 23 * 44
        #     2 3
        # x   4 4
        # -------
        #     9 2
        # + 9 2 0
        # -------
        # 1 0 1 2
        # Time: O(mn) | Space: O(mn)
        m, n = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        digits = [0] * (m + n)

        for i in range(m):
            for j in range(n):
                d1 = self.parse_char(num1[i])
                d2 = self.parse_char(num2[j])
                value = d1 * d2
                k = i + j
                digits[k] += value
                carry = digits[k] // 10
                while carry:
                    digits[k] = digits[k] % 10
                    k += 1
                    digits[k] += carry
                    carry = digits[k] // 10

        result = ''.join(map(str, digits[::-1]))
        i = 0
        while i < len(result) and result[i] == '0':
            i += 1

        result = result[i:]
        return result if len(result) else '0'

    def parse_char(self, char: str) -> int:
        return ord(char) - ord('0')
