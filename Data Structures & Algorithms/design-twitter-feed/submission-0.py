class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timeStamp, tweetId))
        #using max heap so we need to decrement it
        self.timeStamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        #go through every person that this user follows
        self.followMap[userId].add(userId)
        #this step will prepare the heap with the latest tweet values from all of the users
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) -1
                count, tweetId = self.tweetMap[followeeId][index]
                heap.append([count, tweetId, followeeId, index -1])
        
        heapq.heapify(heap)

        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
