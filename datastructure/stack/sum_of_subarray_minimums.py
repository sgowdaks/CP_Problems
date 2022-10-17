class Solution:
    #https://leetcode.com/problems/sum-of-subarray-minimums/discuss/2118729/Very-detailed-stack-explanation-O(n)-or-Images-and-comments
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod=1000000007;
        #next smallest element towards left
        def n_left(arr):
            stack = []
            left_arr = []
            
            for i in range(len(arr)):
                if len(stack) == 0:
                    stack.append(i)
                    left_arr.append(-1)
                elif arr[i] > arr[stack[-1]]:
                    left_arr.append(stack[-1])
                    stack.append(i)
                elif arr[i] <= arr[stack[-1]]:
                    while len(stack) > 0 and   arr[i] < arr[stack[-1]]:
                        stack.pop()
                    if len(stack) == 0:
                        left_arr.append(-1)
                        stack.append(i)
                    else:
                        left_arr.append(stack[-1])
                        stack.append(i)
            return left_arr
        
        #next smallest element towards right
                        
        def n_right(arr):
            right_arr = []
            right_stack = []
            for i in reversed(range(len(arr))):
                if len(right_arr) == 0:
                    right_arr.append(len(arr))
                    right_stack.append(i)
                elif arr[i] > arr[right_stack[-1]]:
                    right_arr.append(right_stack[-1])
                    right_stack.append(i)
                elif arr[i] <= arr[right_stack[-1]]:
                    while len(right_stack) > 0 and arr[i] <= arr[right_stack[-1]]:
                        right_stack.pop()
                    if len(right_stack) == 0:
                        right_arr.append(len(arr))
                    else:
                        right_arr.append(right_stack[-1])
                    right_stack.append(i)
            return right_arr
        
        left_arr = n_left(arr)
        right_arr = n_right(arr)
        
        # print(right_arr)
        
        right_arr = right_arr[::-1]
        
        for i in range(len(left_arr)):
            left_arr[i] = i - left_arr[i]
        
        for i in range(len(right_arr)):
            right_arr[i] = right_arr[i] - i
            
        sum_ = 0
        
        # print(right_arr, left_arr)
        
        for i in range(len(left_arr)):
            # print(left_arr[i], right_arr[i])
            sum_ += (left_arr[i] * right_arr[i] * arr[i])
        
        return sum_%mod        
