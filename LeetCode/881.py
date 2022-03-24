class Solution:
    def numRescueBoats(self, people: List[int], target: int) -> int:
        count = 0
        people = sorted(people)
        i = 0 
        j = len(people) - 1
        print(people)
        while i < j:
            if people[j] > target:
                j = j - 1
            elif people[j] == target:
                count = count + 1
                j = j -1
            elif people[j] + people[i] <= target:
                i = i + 1
                j = j - 1
                count = count + 1
            elif people[j] < target:
                count = count + 1
                j = j - 1
        if j == i and people[i] < target:
            count = count + 1
        return count
                
            
        
