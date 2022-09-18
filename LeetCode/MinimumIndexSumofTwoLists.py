class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:       
        dicti = {}
        for i, val in enumerate(list1):
            dicti[val] = i
            
        dicti1 = {}
        
        min_ = len(list1) + len(list2) - 1
        for i, val in enumerate(list2):
            if val in dicti:
                k = dicti[val] + i
                dicti1[val] = k
                min_ = min(min_, k)
        
        list1 = []
        for i in dicti1.keys():
            # print(i)
            if dicti1[i] == min_:
                list1.append(i)
                
        return list1
