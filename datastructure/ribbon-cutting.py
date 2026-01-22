ribbons = [9, 7, 5] 
k = 4

start = 1
end = max(ribbons)
ans = 0

while start <= end:
    mid = (start+end)//2
    
    total = 0
    for ribbon in ribbons:
        total += (ribbon//mid)
    
    if total == k:
        ans = mid
        start = mid + 1
    if total < k:
        end = mid - 1
    else:
        start = mid + 1

print(ans)
