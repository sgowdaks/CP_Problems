class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        count = 0
        envelopes.sort(key=lambda x:(-x[0],-x[1]))
        # print(envelopes)        
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)-1, -1 , -1):
            for j in range(i+1, len(envelopes)):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], 1+dp[j])
        
        return max(dp)
