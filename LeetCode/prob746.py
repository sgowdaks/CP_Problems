class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = -1
        min_ = 0
        dicti = {}
        cos = self.recurse(cost, len(cost), i, min_, dicti)
        return cos
        
        
        
    def recurse(self, cost, n, i, min_, dicti):
        if i == n - 1 or (i + 1) == n - 1:
            return min_ + cost[i]
        elif i < n-1:
		#this line is very important, because at the begining (-1) we are not counting any cost.
            if i == -1:
                min_ =  min(self.recurse(cost, len(cost), i+1 , min_, dicti), self.recurse(cost, len(cost), i + 2, min_, dicti))
            else:
                if i in dicti:
                    return dicti[i]
            
                min_ = cost[i] + min(self.recurse(cost, len(cost), i+1 , min_, dicti), self.recurse(cost, len(cost), i + 2, min_, dicti))
                if i not in dicti:
                    dicti[i] = min_ 
                
            
        return min_
