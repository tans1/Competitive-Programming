from collections import *
k = input()
rooms = list(input().split())
frequency = defaultdict(int)

for i in rooms:
    frequency[i] += 1

for i in frequency:
    if frequency[i] == 1:
        print(i)
