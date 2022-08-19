arr = [1, 2, 3, -4, -1, 4]
# Output: arr[] = {-4, 1, -1, 2, 3, 4}

def recurse(arr, last, actual):
    tmp = arr[last]
    while actual <= last:
        tmp1 = arr[actual]
        arr[actual] = tmp
        tmp = tmp1
        actual = actual + 1
    
  
def check(arr):      
    pos = 0
    neg = 0
    k = 0
    n = len(arr)
    
    while k < n and neg < n and pos < n:
        if k % 2 == 0:
            if arr[k] > 0:
                neg = k
                pos = k
                while neg < n and arr[neg] > 0:
                    neg = neg + 1
                if neg >= n:
                    return
                recurse(arr, neg, pos)
        else:
            if arr[k] < 0:
                neg = k
                pos = k
                while pos < n and arr[pos] < 0:
                    pos = pos + 1
                if pos >= n:
                    return
                recurse(arr, pos,neg)
        k = k + 1
        
    
check(arr)

print(arr)
