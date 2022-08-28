arr1 = [ 4 , 5 , 2 , 25, -2, 10, 2, 3 , 19, 23 ]

stack = []

arr2 = []

for i in range(len(arr1)):
    if len(stack) == 0:
        arr2.append(-1)
        stack.append(i)
        # stack.append(arr1[i])
    elif arr1[i] > arr1[stack[-1]]:
        #if top < actual element
        while len(stack) > 0 and arr1[i] > arr1[stack[-1]]:
            stack.pop()
        if len(stack) == 0:
            arr2.append(-1)
            stack.append(i)
        else:
            arr2.append(stack[-1])
            stack.append(i)
    elif arr1[i] < arr1[stack[-1]]:
        arr2.append(stack[-1])
        stack.append(i)
    # print(stack)
    # print(arr2)
   
arr3 = []  
for i in range(0, len(arr2)):
    arr3.append(i - arr2[i])

print(arr3)




        
        
        
        
        
    
