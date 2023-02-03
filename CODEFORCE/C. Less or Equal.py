n,k = input().split()
 
arr = list(map(int, input().split()))
arr.sort()
 
if int(k) == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
 
elif int(k) == int(n):
    print(arr[-1])
 
else:
    x = arr[int(k)-1]
 
    if x < arr[int(k)]:
        print(x)
    else:
        print(-1)
