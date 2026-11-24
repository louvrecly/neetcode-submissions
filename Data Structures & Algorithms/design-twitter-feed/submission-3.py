class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)  # mapping followerId -> set[followeeId]
        self.tweetMap = defaultdict(list)  # mapping userId -> tuple[timestamp, tweetId]
        self.timestamp = 0
        self.limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Time: O(1) | Space: O(1)
        self.tweetMap[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Time: O(u + log u) | Space: O(u^2 + u)
        maxHeap = []
        feed = []
        for followeeId in self.followMap[userId]:
            n = len(self.tweetMap[followeeId])
            for i in range(n - 1, max(-1, n - self.limit - 1), -1):
                timestamp, tweetId = self.tweetMap[followeeId][i]
                heapq.heappush_max(maxHeap, (timestamp, tweetId))
        n = len(self.tweetMap[userId])
        for i in range(n - 1, max(-1, n - self.limit - 1), -1):
            timestamp, tweetId = self.tweetMap[userId][i]
            heapq.heappush_max(maxHeap, (timestamp, tweetId))
        while len(feed) < 10 and maxHeap:
            _, tweetId = heapq.heappop_max(maxHeap)
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1) | Space: O(1)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1) | Space: O(1)
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
