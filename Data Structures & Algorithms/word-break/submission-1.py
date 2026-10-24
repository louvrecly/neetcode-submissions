class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word: str):
        node = self
        print(f"word: {word} | node: {node}")
        for char in word:
            print("-" * 5)
            print(f"char: {char} | children: {node.children}")
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s: neetcode | d: [neet code]
        # neet code | T
        # s: applepenapple | d: [apple pen ape]
        # apple pen apple | T
        # s: catsincars | d: [cats cat sin in car]
        # cats in car s | F
        # cat sin car s | F
        # trie/prefix tree
        #      [ ]
        #     / | \
        #    c  i  s
        #    |  |  |
        #    a *n  i
        #   / \    |
        # *r  *t  *n
        #      |
        #     *s
        # c a t s i n c a r s
        # ^ | c | []
        #   ^ | ca | []
        #     ^ | cat | []
        #       ^ | cats | []
        #         ^ | i | [cats]
        #           ^ | in | [cats]
        #             ^ | c | [cats in]
        #               ^ | ca | [cats in]
        #                 ^ | car | [cats in]
        #                    ^ | s | [cats in car]
        #                      ^ | s | [cats in car] | F
        #       ^ | s | [cat]
        #         ^ | si | [cat]
        #           ^ | sin | [cat]
        #             ^ | c | [cat sin]
        #               ^ | ca | [cat sin]
        #                 ^ | car | [cat sin]
        #                   ^ | s | [cat sin car]
        #                     ^ | s | [cat sin car] | F
        # dfs(i, curr, node) = s[i] in node and (
        #     dfs(i + 1, curr + s[i], node[s[i]]) if not node[s[i]].word else
        #     dfs(i + 1, curr + s[i], node[s[i]]) or
        #     dfs(i + 1, '', root)
        # )
        # Time: O(n + mw) | Space: O(n + mw)
        root = TrieNode()
        for word in wordDict:
            root.addWord(word)

        n = len(s)
        curr = []
        memo = {}  # Mapping (i, node) -> bool

        def dfs(i: int, node: TrieNode) -> bool:
            if i >= n:
                return len(curr) == 0

            if (i, node) in memo:
                return memo[(i, node)]

            if s[i] not in node.children:
                memo[(i, node)] = False
                return memo[(i, node)]

            node = node.children[s[i]]
            curr.append(s[i])

            if dfs(i + 1, node):
                memo[(i, node)] = True
                return memo[(i, node)]

            if not node.word:
                memo[(i, node)] = False
                return memo[(i, node)]
    
            curr.clear()
            memo[(i, node)] = dfs(i + 1, root)
            return memo[(i, node)]

        return dfs(0, root)
