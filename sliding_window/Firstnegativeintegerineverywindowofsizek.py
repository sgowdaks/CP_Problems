def printFirstNegativeInteger( A, N, k):
    # code here
    queue = []
    arr = []
    
    for i in range(k-1):
        if A[i] < 0:
            queue.append(A[i])
    
    start = 0
    end = k - 1

    while end < N:
        # print(queue)
        if A[end] < 0:
            queue.append(A[end])
            
        if len(queue) > 0:
            arr.append(queue[0])
        else:
            arr.append(0)
        
        if A[start] < 0:
            queue.pop(0)
            
        start += 1
        end += 1

    return arr
