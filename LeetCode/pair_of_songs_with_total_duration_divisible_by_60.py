class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dicti = {}
        count = 0
        
        for t in time:
            k = t % 60
            if k in dicti:
                dicti[k] += 1
            else:
                dicti[k] = 1
                
        for i in dicti.keys():
            if i <= 30:
                if i == 30 or i == 0:
                    n = dicti[i]
                    count += (n * (n-1))/2
                else:
                    s = 60 - i
                    if s in dicti:
                        count += dicti[i] * dicti[s]
        return int(count)
                
                
        
        # count = 0
        # for i in range(len(time)):
        #     k = time[i]
        #     for j in range(i+1,len(time)):
        #         val = time[i] + time[j]
        #         if (val % 60) == 0:
        #             count += 1
        # return count
