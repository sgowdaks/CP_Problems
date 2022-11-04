class Solution:
    def findMinArrowShots(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        
        #sort it based one the first value
        intervals = sorted(intervals, key=lambda x:x[0])
        count = 1
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        
        #the main logic is when you find a point that has start value greater than your considered/present array value
        #that is the time to reset your values
        # for example: In [[1,6],[2,8],[7,12],[10,16]]
        #6 is the lowest end value of [1,6] and [2,8], so you can blast within that range
        #so reset when you see start time 7
        
        
        for i in range(1, len(intervals)):

            if intervals[i][0] > end:
                count += 1
                start = intervals[i][0]
                end = intervals[i][1]
                
            elif intervals[i][1] < end:
                end = intervals[i][1]
        
        return count
