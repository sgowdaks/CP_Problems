class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[1],x[0]))
        arr = []
        arr.append(intervals[0])
        for i in range(1, len(intervals)):
            k = intervals[i]
                
            if k[0] >= arr[-1][1]:
                arr.append(k)
        
        # print(arr)
        return len(intervals)-len(arr)
