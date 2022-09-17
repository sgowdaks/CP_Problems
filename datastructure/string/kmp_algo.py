def lps(heystack, needle):
    h = len(heystack)
    n = len(needle)
    arr = [0] * n
    prev , cur = 0, 1
    #preprocessing
    while cur < n:
        if needle[cur] == needle[prev]:
            arr[cur] = prev + 1
            prev = prev + 1
            cur = cur + 1
        else:
            if prev == 0:
                arr[cur] = 0
                cur = cur + 1
            else:
                prev = arr[prev - 1]
                
    
    i = 0
    j = 0
    while i < h:
        if heystack[i] == needle[i]:
            i = i + 1
            j = j + 1
        else:
            if j == 0:
                i = i + 1
            else:
                j = arr[j-1]
                
    print(arr)

    
    
