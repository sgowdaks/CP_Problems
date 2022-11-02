class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        dicti1 = {}
        for i in s1:
            if i not in dicti1:
                dicti1[i] = 1
            else:
                dicti1[i] += 1
        
        dicti2 = {}
        for i in s2:
            if i not in dicti2:
                dicti2[i] = 1
            else:
                dicti2[i] += 1
        
        result = []
        
        
        for k in dicti1.keys():
            if dicti1[k] == 1 and k not in dicti2.keys():
                result.append(k)
        
        for k in dicti2.keys():
            if dicti2[k] == 1 and k not in dicti1.keys():
                result.append(k)
                
        # union_ = list1.union(list2)
        # intersection_ = list1.intersection(list2)
        # diff = union_.difference(intersection_)
        # return list(diff)
        
        return result
                
        

        
