n = int(input())
temp = []
for _ in range(n):
    row = list(map(int, input().split()))
    temp.append(row)

sink = []
source = []
for i in range(len(temp)):
    if sum(temp[i]) == 0:
        sink.append(i + 1)
        
for i in range(len(temp[0])):
    sm = 0
    for j in range(len(temp)):
        sm += temp[j][i]
    
    if sm == 0:
        source.append(i + 1)

print(len(source), *source)
print(len(sink), *sink)