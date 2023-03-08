t = int(input())

for _ in range(t):
    a , b = list(map(int, input().split()))

    if max(a,b) >= 3 * min(a,b):  # 3 : 1 ratio
        print(min(a,b))
    else:
        groups = (a + b) // 4
        print(groups)
