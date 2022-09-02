class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0 and num < 9:
            return num
        list1 = []
        if num < 0:
            list1 = str(num)
            list1 = list(list1)
            list1.pop(0)
            list1 = sorted(list1)
            list1 = list1[::-1]
            return (-1)*int(("".join(list1)))
            
        k = num
        count = 0
        while num > 0:
            i = num % 10
            if i == 0:
                count += 1
            else:
                list1.append(str(i))
            num = num // 10
        list1 = sorted(list1)
        while count > 0:
            list1.insert(1, "0")
            count -= 1
        return int("".join(list1))
    
            
        
        
