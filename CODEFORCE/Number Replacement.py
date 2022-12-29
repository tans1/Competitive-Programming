from collections import *
 
 
testcases = int(input())
 
for _ in range(testcases):
    x = int(input())
    dic = defaultdict(list)
    nm = list(map(int,input().split()))
    string = list(input())
    flag = False
 
    for (n,s) in zip(nm,string):
        value = dic[n]
        if len(value) > 0:
            if value[-1] != s:
                print('NO')
                flag = True
                break
            else:
                dic[n].append(s)
        else:
            dic[n].append(s)
            
        
    if flag == False:
        print('YES')
