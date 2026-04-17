import copy

class Twitter:

    def __init__(self):
        self.users = defaultdict(int)
        self.tweets_pq = []
        self.tweet_index = 0

    def createUser(self, userId: int):
        if self.users[userId]:
            return

        self.users[userId] = {
            'tweets': [],
            'followers': set(),
            'following': set()
        }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        self.tweet_index += 1
        self.users[userId]['tweets'].append(tweetId)
        heapq.heappush(self.tweets_pq, (-self.tweet_index, [userId, tweetId]))

    def getNewsFeed(self, userId: int) -> List[int]:
        print(f"GET NEWS FEED FOR user id {userId}")
        res = []
        pq = copy.deepcopy(self.tweets_pq)

        while len(res) < 10 and pq:
            top = heapq.heappop(pq)

            if top[1][0] == userId or top[1][0] in self.users[userId]['following']:
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

        print(self.users)
