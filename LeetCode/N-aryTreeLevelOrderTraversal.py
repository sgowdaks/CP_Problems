class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        else:
            stack = []
            for i in root.children:
                stack.append(i)
            list1 = [[root.val]]
            while len(stack) > 0:
                n = len(stack)
                sub = []
                for i in range(n):
                    popped = stack.pop(0)
                    sub.append(popped.val)
                    for i in popped.children:
                        stack.append(i)
                list1.append(sub)
        return list1
                        
