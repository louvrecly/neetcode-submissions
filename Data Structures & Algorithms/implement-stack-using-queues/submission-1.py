class MyStack:

    def __init__(self):
        self.queue = deque()
        self.store = deque()

    def push(self, x: int) -> None:
        # Time: O(1) | Space: O(1)
        self.queue.append(x)

    def pop(self) -> int:
        # Time: O(n) | Space: O(n)
        while len(self.queue) > 1:
            element = self.queue.popleft()
            self.store.append(element)

        popped = self.queue.popleft()

        while self.store:
            element = self.store.popleft()
            self.queue.append(element)

        return popped

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