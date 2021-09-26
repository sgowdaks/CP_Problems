def shellSort(arr):
    gap = len(arr)//2
    while(gap>0):
        for i in range(gap,len(arr)):
            tmp = arr[i]
            
            j = i
            while(j-gap>-1 and tmp<arr[j-gap]):
                arr[j] = arr[j-gap]
                j = j -gap
            
            arr[j] = tmp
        gap = gap//2
        




arr = [10,4,20,30,19,20,100,299,30,6]
shellSort(arr)
print(arr)
