class Solution:
    def isSubsetSum (self, N, arr, sum_):
        N = N - 1
        max_ = 0
        list2 = []
        
        for i in range(len(arr)):
            list1 = []
            for j in range(sum_+1):
                list1.append(-1)
            list2.append(list1)
            
        def recurse(N, arr, sum_, list2):
            if sum_ == 0:
                return 1
            if N < 0 or max_ > sum_:
                return 0
            else:
                if list2[N][sum_] != -1:
                    return list2[N][sum_]
                k = recurse(N-1, arr, sum_ - arr[N] , list2) | recurse(N-1, arr, sum_, list2)
                list2[N][sum_] = k
                return k
                
                
                
        return recurse(N, arr,  sum_, list2)      
        
