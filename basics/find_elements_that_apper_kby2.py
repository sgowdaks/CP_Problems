arr = [ 1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1 ]

dicti = {}
k= 4

list1 = []

for i in arr:
    if i in dicti:
        dicti[i] += 1
    else:
        dicti[i] = 1

n = len(arr) // 4

print(dicti)
print(len(arr))

for i in dicti.keys():
    if dicti[i] > n:
        list1.append(i)
        
print(list1)
