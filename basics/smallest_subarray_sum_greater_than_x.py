class Solution:
    def smallestSubWithSum(self, arr, n, x):
        # Your code goes here 
        min_count = len(arr)
        count = 0
        
        left = 0
        
        sum_ = 0
        for i in range(0, len(arr)):
            sum_ += arr[i]
            count = count + 1

            while sum_ > x:
                min_count = min(min_count, count)
                # print(product, count)
                sum_ -= arr[left]
                left = left + 1
                count = count - 1
            
            
            
        return min_count
