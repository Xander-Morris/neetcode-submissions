"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)

        for i in range(1, len(intervals)):
            over = intervals[i].start < intervals[i - 1].end 
            if over:
                return False

        return True 