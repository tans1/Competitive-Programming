t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    i = 0
    j = 0
    temp = []
    
    while i < len(arr) and j < len(arr):
        if arr[i] * arr[j] > 0:
            j += 1
        else:
            temp.append(max(arr[i:j]))
            i = j
            j += 1
    temp.append(max(arr[i:j]))
    print(sum(temp))
    
