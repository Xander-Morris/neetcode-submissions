"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start) # sort by start time 
        min_h = []

        for interval in intervals:
            if min_h and min_h[0] <= interval.start:
                # if end time on top of min_heap <= interval.start, then there is no overlap and can share a room, so just pop
                heapq.heappop(min_h)
            heapq.heappush(min_h, interval.end) # push each end time onto heap
        
        return len(min_h)