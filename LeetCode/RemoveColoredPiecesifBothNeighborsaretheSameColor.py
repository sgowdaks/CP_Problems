class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <= 2:
            return False
        colors = list(colors)
        flag = 1
        i = 1
        j = 1
        
        alice = 0
        bob = 0
        
        while i + 1 < len(colors):
            if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
                alice += 1 
            elif colors[i] == "B" and colors[i-1] == "B" and colors[i+1] == "B":
                bob += 1
            i = i + 1           

        if bob > alice:
            return False
            
                
        if alice == bob:
            return False
                
        return True
