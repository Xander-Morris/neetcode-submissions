import copy

class Twitter:

    def __init__(self):
        self.users = defaultdict(int)
        self.tweet_index = 0

    def createUser(self, userId: int):
        if self.users[userId]:
            return

        self.users[userId] = {
            'tweets': defaultdict(int),
            'followers': set(),
            'following': set()
        }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        self.tweet_index += 1
        self.users[userId]['tweets'][tweetId] = self.tweet_index

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        pq = []

        for tweetId in self.users[userId]['tweets']:
            heapq.heappush(pq, (-self.users[userId]['tweets'][tweetId], [userId, tweetId]))

        for otherId in self.users[userId]['following']:
            for tweetId in self.users[otherId]['tweets']:
                heapq.heappush(pq, (-self.users[otherId]['tweets'][tweetId], [otherId, tweetId]))

        while len(res) < 10 and pq:
            top = heapq.heappop(pq)

            if top[1][1] in res:
                continue

            res.append(top[1][1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)
        self.users[followerId]['following'].add(followeeId)
        self.users[followeeId]['followers'].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]['following']:
            self.users[followerId]['following'].remove(followeeId)
        
        if followeeId in self.users and followerId in self.users[followeeId]['followers']:
            self.users[followeeId]['followers'].remove(followerId)