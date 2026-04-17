class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0

        while l <= len(nums) - k:
            pq = []

            for i in range(k):
                index = l + i
                heapq.heappush(pq, (-nums[index], index))

            max_num, _ = heapq.heappop(pq)
            max_num = -max_num
            res.append(max_num)
            l += 1

        return res