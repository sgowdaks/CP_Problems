class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x:x[1])
        passenger = trips[0][0]
        
        #we are storing end kms of a trip and number of passenger into heap
        #By default python heaps are min heap, first trips will be sorted and then the no. of passenger
        #We want to always try to remove maximum number of passenger of any trips that are ending with same time and hence -ve.
        heap = [(trips[0][2], -passenger)]
        
        if passenger > capacity:
            return False
        
        def ending_rides(trip, heap, passenger):
            #This function will check for and remove any rides that is already ended, and also change the total number of passengers you               have currently for further reference
            n, start, end = trip
            while len(heap) > 0 and heap[0][0] <= start:
                tr = heapq.heappop(heap)
                passenger += tr[1]
            return passenger, heap                
        
        
        for i in range(1, len(trips)):
            n, start, end = trips[i]
              
            #for each trip we will check: 1. if the number of passengers are greater than capacity, then return false directly
                                         #2. if not check if you can remove any meeting that is ending at your present trip start time,
                                            #if so then call the function ending_rides
            if trips[i][0] > capacity:
                return False
            else:
                passenger, heap = ending_rides(trips[i], heap, passenger)
                #check if you can add the current ride passengers, if so then add else return false
                if passenger + n <= capacity:
                    passenger += n
                    heapq.heappush(heap, (end, -n))    
                else:
                    return False
        
        return True
                    
        
