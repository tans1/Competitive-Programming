from collections import *
n, m = input().split()
mat = []

for _ in range(int(n)):
    mat.append(list(input()))


columns = list(zip(*mat))
res = ""

for i in range(int(n)):
    horFreq = Counter(mat[i])
    
    for j in range(int(m)):
        verFreq = Counter(columns[j])

        if horFreq[mat[i][j]] == 1 and verFreq[mat[i][j]] == 1:
            res += mat[i][j]
print(res)
    
              
        
