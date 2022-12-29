from collections import *

t = int(input())

for _ in range(t):
    dic = defaultdict(int)
    l,c = input().split()
    orbit = input().split()
    
    for i in range(int(l)):
        dic[orbit[i]] += 1
    res = 0
    for key, value in dic.items():
        if int(c) >= value:
            res += value
        else:
            res += int(c)
    print(res)
        
