class TimeMap:

    def __init__(self):
        # Time: O(1) | Space: O(n)
        self.keyMap = defaultdict(list)  # Mapping key -> (timestamp, value)[]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time: O(1) | Space: O(1)
        self.keyMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Time: O(n) | Space: O(1)
        value = ''
        items = self.keyMap[key]
        if not items:
            return value

        n = len(items)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if items[mid][0] > timestamp:
                right = mid - 1
                continue
            value = items[mid][1]
            if items[mid][0] < timestamp:
                left = mid + 1
            else:
                return value
        return value
