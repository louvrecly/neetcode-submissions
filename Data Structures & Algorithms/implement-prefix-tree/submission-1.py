class Node:
    def __init__(self, char: str):
        self.char = char
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.children = {}  # char -> Node

    def insert(self, word: str) -> None:
        # Time: O(n) | Space: O(n)
        node = self
        for char in word:
            if char not in node.children:        
                node.children[char] = Node(char)
            node = node.children[char]

        node.isEnd = True

    def search(self, word: str) -> bool:
        # Time: O(n) | Space: O(1)
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        # Time: O(n) | Space: O(1)
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
