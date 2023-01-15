rom collections import *
test_case = int(input())
 
for _ in range(test_case):
    n,m = map(int,input().split())
 
    dctMD = defaultdict(int)
    dctOD = defaultdict(int)
    mtr = []
    for _ in range(n):
        row = list(map(int,input().split()))
        mtr.append(row)
 
    for i in range(n):
        for j in range(m):
            dctMD[i-j] += mtr[i][j]
            dctOD[i+j] += mtr[i][j]
    res = 0
 
    for i in range(n):
        for j in range(m):
            res = max(res,(dctMD[i-j] + dctOD[i+j] - mtr[i][j]))
    
    print(res)
