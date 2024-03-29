#maximum area of rectangle in histogram
arr = [[1, 1, 1, 1], [1, 0, 1, 1], [0, 1, 1, 0], [0, 0, 1, 1]]

def get_max(arr):
    left_arr = []
    left_stack = []
    #left next smallest number
    for i in range(len(arr)):
        if len(left_arr) == 0:
            left_arr.append(-1)
            left_stack.append(i)
        elif arr[i] > arr[left_stack[-1]]:
            left_arr.append(left_stack[-1])
            left_stack.append(i)
        elif arr[i] <= arr[left_stack[-1]]:
            while len(left_stack) > 0 and arr[i] <= arr[left_stack[-1]]:
                left_stack.pop()
            if len(left_stack) == 0:
                left_arr.append(-1)
            else:
                left_arr.append(left_stack[-1])
            left_stack.append(i)
    
    #right next smallest number
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
            
    right_arr = right_arr[::-1]
    
    answer = []
    for i in range(len(arr)):
        k = (right_arr[i] - left_arr[i]  -  1)
        answer.append(arr[i]*k)
        
    return max(answer)
    
for i in range(len(arr)):
    if i == 0:
        list1 = arr[0]
        print(list1)
        max_ = get_max(list1)
        print(max_)
    else:
        for k, val in enumerate(arr[i]):
            if val == 0:
                list1[k] = 0
            else:
                list1[k] += val
        # print(list1)
        m = get_max(list1)
        # print(m)
        max_ = max(m, max_)
        
print(max_)
            
        
    
            





