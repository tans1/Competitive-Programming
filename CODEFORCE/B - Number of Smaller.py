n,m = input().split()
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
res = [0]
 
i = 0
j = 0
cnt = 0
 
while i < int(n) and j < int(m):
    if arr2[j] > arr1[i]:
        cnt += 1
        i += 1
    else:
        res.append(res[-1] + cnt)
        j += 1
        cnt = 0
 
while j < int(m):
    res.append(int(n))
    j += 1
print(*res[1:])
