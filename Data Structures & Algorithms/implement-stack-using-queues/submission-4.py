class MyStack:

    def __init__(self):
        self.queue = deque()
        self.store = deque()

    def push(self, x: int) -> None:
        # Time: O(1) | Space: O(1)
        self.queue.append(x)

    def pop(self) -> int:
        # Time: O(n) | Space: O(1)
        n = len(self.queue)
        for _ in range(n - 1):
            self.push(self.queue.popleft())

        return self.queue.popleft()

    def top(self) -> int:
        # Time: O(1) | Space: O(1)
        return self.queue[-1]

    def empty(self) -> bool:
        # Time: O(1) | Space: O(1)
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()