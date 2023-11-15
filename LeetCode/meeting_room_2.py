import heapq
#https://leetcode.com/problems/meeting-rooms-ii/discuss/1529030/Easy-Python-3-w-Explanation%3A-Min-Heap-O(nlogn)
class Solution:    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        intervals = sorted(intervals, key=lambda x:x[0])
        count = 1
        interval = []
        
        count = 1
        
        print(intervals)
        
        heap = [intervals[0][1]]
        
        for i in range(1, len(intervals)):
            earlist_end = heap[0]
            
            if intervals[i][0] >= earlist_end:
                heapq.heapreplace(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
        
        print(heap)
        return len(heap)
