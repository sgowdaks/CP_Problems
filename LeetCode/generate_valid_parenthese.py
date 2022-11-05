class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def check_for(s, left, right):
            # print(s)
            if left == 0 and right == 0:
                ans.append(s)
                return
            
            if left > 0:
                check_for(s + "(", left - 1, right)
            if right > left and right > 0:
                check_for(s + ")", left, right - 1)
            
        
        check_for("(", n-1, n)
        return ans
