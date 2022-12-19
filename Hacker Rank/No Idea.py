# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
happiness = 0
lst =[int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

for i in lst:
    happiness += i in A
for j in lst:
    happiness -= j in B
print(happiness)
