class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        max_ = 0
        for event in events:
            max_ = max(max_, event[1])
        
        events.sort(key = lambda x:(x[0], x[1]))
        heap = []
        events_no = 0
        even = 0
      
        for i in range(1, max_ + 1):
            
            while events_no < len(events) and events[events_no][0] == i:
                heapq.heappush(heap, events[events_no][1])
                events_no += 1
            
            while len(heap) > 0 and heap[0] < i:
                heapq.heappop(heap)
            
            if heap and heap[0] >= i:
                heapq.heappop(heap)
                even += 1
                
        return even
        
        #solution that gives TLE error
        
        
        # events = sorted(events, key=lambda x: x[1])
        # visited = set()
        # for s, e in events:
        #     for t in range(s, e+1):
        #         if t not in visited:
        #             visited.add(t)
        #             break
        # return len(visited)
