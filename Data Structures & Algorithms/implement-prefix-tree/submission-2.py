class PrefixTree:

    def __init__(self):
        self.children = {}  # char -> Node
        self.isEnd = False

    def insert(self, word: str) -> None:
        # Time: O(n) | Space: O(n)
        node = self
        for char in word:
            if char not in node.children:        
                node.children[char] = PrefixTree()
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
