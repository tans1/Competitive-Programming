from collections import *


def addEdge(u,v):
    graph[u].append(v)
    graph[v].append(u)
    

graph = defaultdict(list)
n = int(input())
k = int(input())

for _ in range(k):
    temp = list(map(int, input().split()))
    
    if temp[0] == 1:
        addEdge(temp[1],temp[2])
    elif temp[0] == 2:
        if temp[1] in graph:
            print(*graph[temp[1]])
