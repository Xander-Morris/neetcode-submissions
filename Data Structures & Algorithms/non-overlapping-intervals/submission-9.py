class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        to_remove = 0
        intervals.sort(key = lambda x: x[1]) # sort by end
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if start < prev_end:
                to_remove += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end 

        return to_remove