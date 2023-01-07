# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split(' ')))
    
    i = 0
    j = n - 1
    base = max(blocks[i], blocks[j])
    flag = False
    while i <= j:
        if blocks[i] <= base and blocks[i] >= blocks[j]:
            base = blocks[i]
            i += 1
        elif blocks[j] <= base:
            base = blocks[j]
            j -= 1
        else:
            print('No')
            flag = True
            break
    if not flag:
        print('Yes')
