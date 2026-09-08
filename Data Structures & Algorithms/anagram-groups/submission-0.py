class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # act, pots, tops, cat, stop, hat
        # act -> a: 1, c: 1, t: 1
        # pots -> o: 1, p: 1, s: 1, t: 1
        counterMap = {}  # Mapping counter -> [s]

        for word in strs:
            counter = [0] * 26  # counts of each char (a-z)
            for char in word:
                counter[ord(char) - ord('a')] += 1
            counterTuple = tuple(counter)
            counterMap[counterTuple] = counterMap.get(counterTuple, [])
            counterMap[counterTuple].append(word)

        return list(counterMap.values())
