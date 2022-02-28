class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_ = min(time)
        r = min_ * totalTrips
        l = min_
        trip = 0
        while l < r:
            trip = 0
            mid =  (r + l) // 2
            for i in time:
                trip = trip + (mid // i)
            if trip < totalTrips:
                l = mid + 1
            else:
                r = mid            
        return l
                
            
        
        
