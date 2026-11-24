class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)  # mapping followerId -> set[followeeId]
        self.tweetMap = defaultdict(list)  # mapping userId -> list[tweetId]
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Time: O(1) | Space: O(1)
        self.tweetMap[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Time: O(u) | Space: O(u)
        maxHeap = []
        feed = []
        followeeIds = self.followMap[userId]
        followeeIds.add(userId)
        for followeeId in followeeIds:
            if self.tweetMap[followeeId]:
                n = len(self.tweetMap[followeeId])
                timestamp, tweetId = self.tweetMap[followeeId][n - 1]
                heapq.heappush_max(maxHeap, (timestamp, tweetId, followeeId, n - 1))
        while len(feed) < 10 and maxHeap:
            _, tweetId, followeeId, i = heapq.heappop_max(maxHeap)
            feed.append(tweetId)
            if i > 0:
                timestamp, tId = self.tweetMap[followeeId][i - 1]
                heapq.heappush_max(maxHeap, (timestamp, tId, followeeId, i - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1) | Space: O(1)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1) | Space: O(1)
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
