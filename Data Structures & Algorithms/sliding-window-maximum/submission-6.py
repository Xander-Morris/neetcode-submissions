class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        pq = []
        l = 0

        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))

        for l in range(len(nums)):
            heapq.heappush(pq, (-nums[l], l))

            if l >= k - 1:
                while pq[0][1] <= l - k:
                    heapq.heappop(pq)
                
                res.append(-pq[0][0])

        return res