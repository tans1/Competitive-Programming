n,m = input().split()
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
  
res = []
i = 0
j = 0
while i < int(n) and j < int(m):
    if arr1[i] < arr2[j]:
        res.append(arr1[i])
        i += 1
    else:
        res.append(arr2[j])
        j += 1
 
res.extend(arr1[i:])
res.extend(arr2[j:])
print(*res)
