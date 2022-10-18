#https://leetcode.com/problems/sum-of-subarray-ranges/discuss/1626628/O(n)-solution-with-monotonous-stack-oror-Full-explaination
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        #smallest towards left 
        def nsl(nums):
            arr = []
            stack = []
            for i in range(len(nums)):
                if len(stack) == 0:
                    stack.append(i)
                    arr.append(-1)
                elif nums[i] > nums[stack[-1]]:
                    arr.append(stack[-1])
                    stack.append(i)
                elif nums[i] <= nums[stack[-1]]:
                    while len(stack) > 0 and nums[i] < nums[stack[-1]]:
                        stack.pop()
                    if len(stack) == 0:
                        arr.append(-1)
                        stack.append(i)
                    else:
                        arr.append(stack[-1])
                        stack.append(i)                
            
            return arr
        
        #smallest towards right
        def nsr(nums):
            arr = []
            stack = []
            
            for i in reversed(range(len(nums))):
                if len(stack) == 0:
                    stack.append(i)
                    arr.append(len(nums))
                elif nums[i] > nums[stack[-1]]:
                    arr.append(stack[-1])
                    stack.append(i)
                elif nums[i] <= nums[stack[-1]]:
                    while len(stack) > 0 and nums[i] <= nums[stack[-1]]:
                        stack.pop()
                    if len(stack) == 0:
                        arr.append(len(nums))
                        stack.append(i)
                    else:
                        arr.append(stack[-1])
                        stack.append(i) 
            return arr[::-1]
        
        #highest towards left
        def nll(nums):
            arr = []
            stack = []
            for i in range(len(nums)):
                if len(stack) == 0:
                    stack.append(i)
                    arr.append(-1)
                elif nums[i] < nums[stack[-1]]:
                    arr.append(stack[-1])
                    stack.append(i)
                elif nums[i] >= nums[stack[-1]]:
                    while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                        stack.pop()
                    if len(stack) == 0:
                        arr.append(-1)
                        stack.append(i)
                    else:
                        arr.append(stack[-1])
                        stack.append(i)                
            
            return arr
        
        #highest towards right
        def nlr(nums):
            arr = []
            stack = []
            
            for i in reversed(range(len(nums))):
                # print(i, len(stack), stack)
                if len(stack) == 0:
                    stack.append(i)
                    arr.append(len(nums))
                elif nums[i] < nums[stack[-1]]:
                    arr.append(stack[-1])
                    stack.append(i)
                elif nums[i] >= nums[stack[-1]]:
                    while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                        stack.pop()
                    if len(stack) == 0:
                        arr.append(len(nums))
                        stack.append(i)
                    else:
                        arr.append(stack[-1])
                        stack.append(i)  
            return arr[::-1]
        
        nsl = nsl(nums)
        nsr = nsr(nums)
        nll = nll(nums)
        nlr = nlr(nums)
        
        for i in range(len(nsl)):
            nsl[i] = i - nsl[i]
            nsr[i] = nsr[i] - i
            nll[i] = i - nll[i]
            nlr[i] = nlr[i] - i
        
        sum_ = 0
        for i in range(len(nsl)):
            k = (nll[i]*nlr[i]) - (nsr[i]*nsl[i])
            sum_ += (k*nums[i])
        
        return sum_
