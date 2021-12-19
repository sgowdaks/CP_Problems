class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max = nums[0]
        NewMax = nums[0]
        for i in range(1,len(nums)):
            Newsum = nums[i] + Max
            if(nums[i] > Newsum):
                Max = nums[i]
                if Max > NewMax:
                    NewMax = Max
            else:
                Max = Newsum
                if Max > NewMax:
                    NewMax = Max
            #print(NewMax)
                
        return NewMax
      
#kadanes Algorithm
