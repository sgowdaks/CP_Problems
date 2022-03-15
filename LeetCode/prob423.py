class Solution:
    def originalDigits(self, s: str) -> str:
        arr = []
        for i in range(10):
            arr.append(0)
        st = ""
        s = list(s) 
        arr[0] = s.count('z')
        arr[2] = s.count('w')
        arr[4] = s.count('u')
        arr[6]= s.count('x')
        arr[8] = s.count('g')
        arr[1] = s.count('o') - arr[0] - arr[2] - arr[4]
        arr[3] = s.count('r') - arr[4] - arr[0]
        arr[5] = s.count('f') - arr[4]
           arr[7] = s.count('v') - arr[5]
        arr[9] =  int((s.count('n') - arr[1] - arr[7])/2)
        for i in range(len(arr)):
            if arr[i] > 0:
                st = st + str(i) * arr[i]
                print(str(i)*5)
        return st
