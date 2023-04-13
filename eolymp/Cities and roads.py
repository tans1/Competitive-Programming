from collections import *


graph = defaultdict(list)
grid = []
n = int(input())
for _ in range(n):
    row = list(map(int,input().split()))
    grid.append(row)

for i in range(len(grid)):
    for j in range(i+1, len(grid[0])):
        if grid[i][j] == 1:
            graph[i+1].append(j+1)

ans = 0
for k, v in graph.items():
    ans += len(v)
print(ans)
