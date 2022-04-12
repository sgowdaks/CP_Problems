class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        val = []
        weight = []
        ratio = []
        newlist1 = []
        for i in range(n):
            val = Items[i].value
            weight = Items[i].weight
            ratio = val/weight
            newlist1.append([val, weight, ratio])
        #print(newlist1)
        newlist1.sort(key = lambda x: x[2], reverse=True)
        # print(newlist1)
        w_ = 0
        val = 0
        for i in range(n):
            if w_ == W:
                return val
            if w_ + newlist1[i][1] <= W:
                w_ += newlist1[i][1]
                val += newlist1[i][0]
                #print(i, w_, val)
            else:
                if w_ + newlist1[i][1] > W:
                    extra = w_ + newlist1[i][1] - W
                    nw = newlist1[i][1] - extra
                    k = (nw * newlist1[i][0]) / newlist1[i][1]
                    # print(k)
                    val += k
                    w_ = w_ + nw
                    #print(i, w_, val)
                    return val
                    #print(i, w_, val)
        return val
