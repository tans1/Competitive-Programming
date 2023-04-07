n =  int(input())
arr = list(map(int, input().split()))
odd = False
even = False
for n in arr:
    even = (even or n % 2 == 0)
    odd = (odd or n % 2 != 0)


if odd and even:
    arr.sort()
    print(*arr)

else:
    print(*arr)
