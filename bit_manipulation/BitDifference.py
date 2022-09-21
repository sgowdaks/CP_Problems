class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        flip = 0
        while a > 0 or b > 0:
            k1 = a & 1
            k2 = b & 1
            # print(k1, k2)
            if k1 != k2:
                flip += 1
            a = a >> 1
            b = b >> 1
        
        return flip
