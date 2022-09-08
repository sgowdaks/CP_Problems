#method 1
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
      output = []
      queue = []
      for i in range(1, 10):
        queue.append([i])
      
      while queue:
        l = queue.pop(0)
        if len(l) == n:
          st = [st(i) for i in l]
          output.append(int("".join(st)))
        else:
          nx = l[-1] + k
          if nx >= 0 and nx <= 9:
            queue.append(l + [nx])
          nx = l[-1] - k
          if nx >= 0 and nx <= 9:
            queue.append(l + [nx])
      return set(output)
          
        
#method 2
def check_for(num, n, k, count, main, list1, val):
            if count == n:
                list1.add(val)
            else:
                val += str(num)
                count = count + 1
                if num + k <= 9:
                    check_for(num + k, n, k, count, main, list1, val)
                if num - k >= 0:
                    check_for(num - k, n, k, count, main, list1, val)
                return
                
                
        
        s = set()
        for i in range(1, 10):
            count = 0
            main = i
            check_for(i, n, k, count, main, s, val = "")
        return s
