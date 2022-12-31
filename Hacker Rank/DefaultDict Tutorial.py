# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
n,m = input().split()
dct = defaultdict(list)

for i in range(int(n)):
    a = input()
    dct[a].append(str(i+1))


for j in range(int(m)):
    b = input()
    if dct[b] == []:
        print(-1)
    else:
        print(' '.join(dct[b]))
