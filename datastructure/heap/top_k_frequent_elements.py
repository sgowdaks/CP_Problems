class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heap
        dicti = {}
        for num in nums:
            if num in dicti:
                dicti[num] += 1
            else:
                dicti[num] = 1
        
        heap = [(-value, key) for key, value in dicti.items()]
        
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
              
        #bucket sort
        dicti = {}
        for num in nums:
            if num in dicti:
                dicti[num] += 1
            else:
                dicti[num] = 1
                
        arr = [0]*(len(nums)+1)
                
        for key, value in dicti.items():
            if arr[value] == 0:
                arr[value] = [key]
            else:
                # print(arr)
                arr[value].append(key)
                
        result = []
                    
        for i in reversed(range(len(arr))):
            if len(result) == k:
                return result
            if arr[i] != 0:
                for i in arr[i]:
                    result.append(i)
        return result
        
