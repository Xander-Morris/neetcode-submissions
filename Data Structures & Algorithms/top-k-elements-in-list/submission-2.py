class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        pq = []

        for num in set(nums):
            print(f"Num: {num} with count of {count[num]}")
            heapq.heappush(pq, (-count[num], num))

        i = 0
        while pq and i < k:
            pri, task = heapq.heappop(pq)
            print(str(pri) + " and task of " + str(task))
            result.insert(len(result), task)
            i += 1

        return result