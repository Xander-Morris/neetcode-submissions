import bisect

class MedianFinder:

    def __init__(self):
        self._nums = []

    def addNum(self, num: int) -> None:
        i = bisect.bisect_left(self._nums, num)
        self._nums.insert(i, num)

    def findMedian(self) -> float:
        n = len(self._nums)
        return self._nums[n // 2] if n % 2 != 0 else (self._nums[n // 2] + self._nums[(n // 2) - 1]) / 2