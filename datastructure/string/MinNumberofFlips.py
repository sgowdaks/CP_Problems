class Solution:
    def minFlips(self, S):
        # Code here
        S = [int(i) for i in S]
        list1 = [0] * len(S)
        list2 = [0] * len(S)
        
        for i in range(len(list1)):
            if i % 2 == 0:
                list1[i] = 1
            else:
                list2[i] = 1
        
        count1 = 0
        count2 = 0
        
        # print(list1, list2, S)
        
        for i in range(len(S)):
            if S[i] != list1[i]:
                count1 += 1
            if S[i] != list2[i]:
                count2 += 1
        
        return min(count1, count2)
