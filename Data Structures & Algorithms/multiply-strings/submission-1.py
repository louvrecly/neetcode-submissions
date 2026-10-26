class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # num1: 3 | num2: 4
        # 3 * 4 = 12
        # num1: 20 | num2: 5
        # 20 * 5 = 100
        # 2 0 | 2*10 + 0 = 20
        # 5 | 5 = 5
        # return str(int(num1) * int(num2))
        # Time: O(log num1 num2) | Space: O(1)
        def to_int(num_str: str) -> int:
            num = 0
            for char in num_str:
                num = 10 * num + ord(char) - ord('0')
            return num

        product = to_int(num1) * to_int(num2)
        return str(product)
