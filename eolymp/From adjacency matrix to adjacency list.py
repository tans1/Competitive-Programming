from collections import *

n = int(input())
temp = []
for _ in range(n):
    row = list(map(int, input().split()))
    temp.append(row)
lst = defaultdict(list)
for i in range(len(temp)):
    for j in range(len(temp[0])):
        if temp[i][j] == 1:
            lst[i+1].append(j+1)

for  k, v in lst.items():
    v.sort()
    print(len(v), *v)
