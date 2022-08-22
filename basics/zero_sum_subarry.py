class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        
        count = 0
        
        dicti = {}
        dicti[0] = 1
        sum_ = 0
        
        for i in range(len(arr)):
            sum_ = sum_ + arr[i]
            if sum_ in dicti:
                count += dicti[sum_]
                dicti[sum_] += 1
            else:
                dicti[sum_] = 1
                
        return count
