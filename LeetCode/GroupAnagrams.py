from collections import defaultdict
  
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = defaultdict(list)
        for word in strs:
            count = [0] * 26
            
            for i in word:
                count[ord(i) - 97] += 1
            list1[tuple(count)].append(word)
        
        return list1.values()
