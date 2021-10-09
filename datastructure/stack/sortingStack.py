# Implementing stack from the scratch


def sortedStack(stack,curr):
    if len(stack)==0 or curr>stack[-1]:
        stack.append(curr)
        #print(element)
        return
    else:
        tmp = stack.pop()
        sortedStack(stack,curr)
        stack.append(tmp)
    


def sort(stack):
    if(len(stack)!=0):
        tmp = stack.pop()
        #print(stack)
        sort(stack)
        sortedStack(stack,tmp)
        #print(stack)
        
    
        
stack = []

stack.append("c")
stack.append("d")
stack.append("a")
stack.append("e")
stack.append("b")
k = len(stack)

#print(k)

print(stack)
sort(stack)
print(stack)


