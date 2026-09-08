class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for string in strs:
            n = len(string)
            s += f"{n}:{string}"
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            n = int(s[i:j])
            strs.append(s[j + 1:j + n + 1])
            i = j + n + 1
        return strs
