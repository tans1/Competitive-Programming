# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(input().split())
A1 = [int(i) for i in a]

A = set(A1)
n = int(input())
i = 0
while i < n:
    b = list(input().split())
    B1 = [int(i) for i in b]
    
    B = set(B1)
    if B.issubset(A) == False or len(A - B) == 0:
        print(False)
        break
    i += 1
else:
    print(True)
