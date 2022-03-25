
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        def bag(n , W, val, wt):
            # print(n,W)    
            if n < 0 or W == 0:
                return 0

            if wt[n] > W:
                return bag(n-1, W, val, wt)
                
            else:
                # print(n,W)
                if list1[n][W] != -1:
                    return list1[n][W]
                k = max(val[n] + bag(n-1, W - wt[n], val, wt), bag(n-1, W, val, wt))
                list1[n][W] = k
                return k
        
        w = 0
        list1 = []
        for i in range(n):
            list2 = []
            for j in range(W+1):
                list2.append(-1)
            list1.append(list2)
        #print(len(list1), len(list1[0]))
        n = n - 1
        return bag(n, W, val, wt)
