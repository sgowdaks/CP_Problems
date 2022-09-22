class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        # code here
        list1 = []
        max_ = 0
        for i in Jobs:
            max_ = max(max_, i.deadline)
            list1.append([i.deadline, i.profit])
        list1.sort(key=lambda x:(-x[1]))  
        # print(list1)
        
        
        profit = 0
        count = 0
        
        dp = {}
        
        tabel = [0] * len(list1)
        #method1 while using maximum space
        # print(tabel)
        # tabel = [0] * max_
        
        # for i in range(len(list1)):
        #     if tabel[list1[i][0] - 1] == 0:
        #         profit += list1[i][1]
        #         tabel[list1[i][0] - 1] = 1
        #         count += 1
        #     else: 
        #         n = list1[i][0] - 1
        #         if n in dp:
        #             continue
        #         else:
        #             flag = 0
        #             while n >= 0:
        #                 if tabel[n] == 0:
        #                     profit += list1[i][1]
        #                     tabel[n] = 1
        #                     count += 1
        #                     flag = 1
        #                     break
        #                 else:
        #                     n = n - 1
        #             if flag == 0:
        #                 dp[list1[i][0] - 1] = 0
                        
        # return count, profit
        
        
        #method2 while using jobs size space
        for i in range(len(list1)):
            # print(list1[i][0] - 1)
            if list1[i][0] - 1 < len(tabel) and tabel[list1[i][0] - 1] == 0:
                profit += list1[i][1]
                tabel[list1[i][0] - 1] = 1
                count += 1
            else: 
                n = min(len(tabel)-1, list1[i][0] - 1)
                k = n
                if k in dp:
                    continue
                else:
                    flag = 0
                    while n >= 0:
                        if tabel[n] == 0:
                            profit += list1[i][1]
                            tabel[n] = 1
                            count += 1
                            flag = 1
                            break
                        else:
                            n = n - 1
                    if flag == 0:
                        dp[k] = 0
                        
        return count, profit
