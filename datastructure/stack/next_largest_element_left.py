arr1 = [ 4 , 5 , 2 , 25, -1, 10, 2, 3 , 19, 23 ]

stack = []

for i in range(len(arr1)):
    if len(stack) == 0:
        print(-1)
        stack.append(arr1[i])
    elif stack[len(stack)-1] > arr1[i]:
        print(stack[len(stack)-1])
        stack.append(arr1[i])
    elif stack[len(stack)-1] < arr1[i]:
        while len(stack) != 0 and stack[len(stack)-1] < arr1[i]:
            stack.pop()
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
        stack.append(arr1[i])
        
    
