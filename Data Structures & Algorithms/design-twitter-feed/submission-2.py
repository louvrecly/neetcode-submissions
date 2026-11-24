class Tweet:
    def __init__(self, userId, tweetId):
        self.id = tweetId
        self.userId = userId


class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)  # mapping followerId -> set[followweeId]
        self.tweets = []  # sorted tuple (timestamp, userId, tweetId)
        self.time = 0
        self.limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Time: O(1) | Space: O(1)
        tweet = Tweet(userId, tweetId)
        self.tweets.append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        # Time: O(n) | Space: O(n)
        followees = self.follows[userId].copy()
        followees.add(userId)
        feed = []
        tweets = self.tweets.copy()
        while len(feed) < self.limit and tweets:
            tweet = tweets.pop()
            if tweet.userId in followees:
                feed.append(tweet.id)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1) | Space: O(1)
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Time: O(1) | Space: O(1)
        self.follows[followerId].discard(followeeId)
