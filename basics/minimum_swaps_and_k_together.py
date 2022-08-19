def minSwap (arr, n, k) : 
    #Complete the function
    nums = 0
    for i in arr:
        if i <= k:
            nums += 1
    
    if nums == 0:
        return 0
        
    if nums == len(arr):
        return 0
    
    swaps = 0
    for i in range(0, nums):
        if arr[i] > k:
            swaps += 1
            
    min_swap = swaps
    
    left = 0
    right = nums

    while right < len(arr):
        if arr[left] <= k:
            swaps = swaps + 1
        if arr[right] <= k:
            swaps = swaps - 1
        
        left = left + 1
        right = right + 1
        min_swap = min(min_swap, swaps)
    
    return min_swap
