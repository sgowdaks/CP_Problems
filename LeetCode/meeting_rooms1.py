class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 1 or len(intervals) == 0:
            return True
        intervals = sorted(intervals, key = lambda x:x[1])
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                start, end = intervals[i]
            else:
                return False
        return True
