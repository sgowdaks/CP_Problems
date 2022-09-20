class Solution:
    def countBits(self, n: int) -> List[int]:
        #observation
        binary = [0] * (n+1)
        for i in range(1, n+1):
            #if even
            if i % 2 == 0:
                val = i // 2
                # print(i, val)
                binary[i] = binary[val] 
            else:
                #if odd
                val = i // 2
                binary[i] = binary[val] + 1
        return binary
